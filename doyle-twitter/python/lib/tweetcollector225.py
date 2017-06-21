#!/usr/bin/python
# -*- coding: utf-8 -*-

#TweetCollector is a Twitter scraper built on the SeeTweet functions
# However, it retains all tweets (not only mappable ones), although it still tries to map
# Its tweet formatting is also different (tab separation in the tweetarchive files).
#The structure of TC is the same as SeeTweet and should retain all ST functionality for re-integration if I have any really good ideas.
# The defaults will change, however.  Specifically:
#  raw is the default
#  scheduled is the default

#v. 2.2.5 has essentially no changes from 2.2.2 but has been update to work on the sherlock cluster

from seetweetlib225 import *
from pprint import pprint

################################################################################
#
# Recognizing additional options
#
################################################################################

#loclist = ["39.8,-98.6"]
loclist = ["30.8,-98.6","39.8,-95.6","32.8,-117.6","37.8,-122.6"]
radius = "2500km"
multiloc = True
tweetspersearch = 50
maxpages = 20
maxid = float("+inf")
importcsv = ''
overwrite = 'w'
outfile = ''
keeptweets = True
startat = 0
header = True
throttle = True
checklimits = 3 		#To avoid overquerying the rate_limit function, only check every N iterations
importmultiloc = False
newmultiloc = False
onlyincltweets = True
wff = False
trackfails = False
MAXERRORS = 3
scheduled = True
raw = True

if (len(sys.argv) > 2):
	for arg in sys.argv[2:]:
		tag = arg[0:2]
		featval = arg[3:]
		if tag == '-l':					#-l: latitude,longitude pair
			loclist = [featval]				#e.g., -l=39.8,-98.6
			multiloc = False
		elif tag == '-r':				#-r: radius
			radius = featval				#e.g., -r=2500km
		elif tag == '-p':				#-p: max number of search pages (1/50 number of tweets)
			maxpages = int(featval)			#e.g., -p=20
		elif tag == '-b':				#-b: return tweets before this tweetid
			maxid = long(featval)			#e.g., -b=1032034034
		elif tag == '-c':				#-c: import tweetids from a separate csv
			importcsv = featval				#e.g., -c=needs+done.csv
		elif tag == '-t':				#-t: change number of tweets requested per search
			tweetspersearch = int(featval)
		elif tag == '-a':				#-a: append results to existing outfile
			overwrite = 'a+'
			header = False
		elif tag == '-f':				#-f: specify outfile name (incl. extension)
			outfile = featval
		elif tag == '-k':				#-k: don't keep an archive of found tweets for re-processing
			keeptweets = False
		elif tag == '-s':				#-s: start with tweet number... (to be used with -c tag)
			startat = int(featval)
			overwrite = 'a+'
			header = False
		elif tag == '-h':				#-h: omit commented header on csv file 
			header = False
		elif tag == '-T':				#-T: turn throttling off
			throttle = False
		#elif tag == '-L':				#-L: use the four locations that cover the U.S.
		#	loclist = ["30.8,-98.6","39.8,-95.6","32.8,-117.6","37.8,-122.6"]
		#	multiloc = True
		elif tag == '-e':				#-e: remove excluded tweets (incl=0) when constructing a baseline
			onlyincltweets = False
		elif tag == '-F':				#-F: record locations that aren't mappable (for debugging purposes)
			trackfails = True
		elif tag == '-S':				#-S: for scheduled searches, save files with timestamps
			scheduled = True
		elif tag == '-R':				#-R: 'raw' tweet storage for corpus creation; includes non-locatable tweets, uses tab-separation instead of CSV on *.tweets files
			raw = True
			keeptweets = True
		else:
			raise ValueError("Inappropriate option "+tag)

tweetcount = 0

if (importcsv and multiloc):
	importmultiloc = True
elif multiloc:
	newmultiloc = True


if importcsv:
	rf = open(importcsv,'r')
	firstline=True
	tidnum = 0
	tids = []
	centers = []
	incls = []
	for line in rf:
		if line[0] == '#':
			continue
		splitline = line.strip().split(',')
		if firstline:
			tidnum = splitline.index('tid')
			if importmultiloc:
				centernum = splitline.index('center')
				inclnum = splitline.index('incl')
			firstline=False
		else:
			if onlyincltweets:							#If we're excluding excluded tweets from baseline calc, skip to next line if incl=0
				if int(splitline[inclnum])==0:
					continue
			tids.append(long(splitline[tidnum])-1)
			if importmultiloc:
				centers.append(int(splitline[centernum]))
				incls.append(int(splitline[inclnum]))
	tids = tids[startat:]
	if importmultiloc:
		centers = centers[startat:]
		incls = incls[startat:]
	maxpages = len(tids)
	tids.append(0)
	firsthit = tids[0]
	rf.close()
else:
	firsthit = float("+inf")

outcomes = {}
locnum = -1
if newmultiloc:
	tweetlist = [0]*len(loclist)
	searchesleft = [0]*len(loclist)
	mintids = [0]*len(loclist)
	maxtids = [0]*len(loclist)
elif importmultiloc:
	tweetlist = [0]*maxpages		#tweetlist[tweetnum][locnum][resnum] = [outline,loc,tid] for the resnum-th baseline tweet in loc locnum on testtweet tweetnum
	mintids = [0]*maxpages
	maxtids = [0]*maxpages
	
	
#Establishing the search & opening to output files
term1 = sys.argv[1]
term = re.sub('\"','%22',term1)

tsearch = authorize()

if importcsv:
	if not outfile:
		outfile = 'base.'+term1.strip('\"')+'.'+importcsv
else:
	if scheduled:
		scheddir = 'scheduled'
		if not os.path.exists(scheddir):
			os.mkdir(scheddir)
		outfile = scheddir+'/'+term1.strip('\"')+'.'+strftime('%Y%m%d.%H%M')+'.csv'
	if not outfile:
		outfile = term1.strip('\"')+'.csv'
wf = open(outfile,overwrite)
latlong = loclist[0]
if header:
	wf.write('#Compiled by SeeTweet '+versionnum+'.\n')
	wf.write('#Search performed at '+strftime('%Y-%m-%d %H:%M')+'\n')
	if not multiloc:
		wf.write('#Search location: '+latlong+','+radius+'\n')
	else:
		wf.write('#Search location: U.S. 4-location coverage points (Texas, KC, SD, SF)\n')
	wf.write('#Search term: '+term1+'\n')
if (overwrite=='w' and not multiloc):
	wf.write('day,year,month,date,hour,minute,second,source,city,state,lat,long,uid,tid\n')
elif (overwrite=='w' and newmultiloc):
	wf.write('day,year,month,date,hour,minute,second,source,city,state,lat,long,uid,tid,center,incl\n')
elif (overwrite=='w' and importmultiloc):
	wf.write('day,year,month,date,hour,minute,second,source,city,state,lat,long,uid,tid,origtid,origincl,center,incl\n')
if keeptweets:
	tweetdir = 'tweetarchive'
	if not os.path.exists(tweetdir):
		os.mkdir(tweetdir)
	if not os.path.exists(tweetdir+'/'+scheddir):
		os.mkdir(tweetdir+'/'+scheddir)
	outtweetfile = tweetdir+'/'+os.path.splitext(outfile)[0]+'.tweets'
	wft = open(outtweetfile,overwrite)
	if overwrite=='w':
		if raw:
			wft.write('day\tyear\tmonth\tdate\thour\tminute\tsecond\tloc\tuid\ttid\ttweet\ttlength\trt\n')
		else:
			wft.write('loc,uid,tid,tweet\n')
if trackfails:
	faildir = 'failures'
	if not os.path.exists(faildir):
		os.mkdir(faildir)
	outfailfile = faildir+'/'+os.path.splitext(outfile)[0]+'.fails'
	wff = open(outfailfile,'w')
	
	
	
	
for latlong in loclist:
	locnum = locnum + 1
	geocodestr = latlong+","+radius
	print "\nSearch centered at:", latlong, "(locnum "+str(locnum)+")"
	if newmultiloc:
		currloctweets = []
		tidbycurrloc = []
	
	for pagenum in range(0,maxpages):
		print ''
		if importmultiloc:
			if (locnum==0):
				tweetlist[pagenum] = []
				maxtids[pagenum] = []
				mintids[pagenum] = []
			#print maxtids
			currloctweets = []
			tidbycurrloc = []
		#Examining the rate limit
		if (pagenum % checklimits == 0):
			r = getlimits(tsearch)
			if r['remaining'] <= checklimits:
				print "\n\n**Paused because of rate limit.**"
				print "Current time:",strftime('%I:%M:%S')
				print "Reset time:  ",strftime('%I:%M:%S',localtime(r['reset']))
				if not multiloc:
					print "Resume with flag -s="+str(startat+pagenum)
				else:
					print "Stopped on location "+str(locnum)+", tweet "+str(startat+pagenum)+"/"+str(maxpages)
				print "--"
				print tweetcount, 'tweets found. Centered at', geocodestr
				print outcomes
				if throttle:
					waittime = r['reset']-time()+30
					print "Waiting", round(waittime), "seconds before resuming."
					sleep(waittime)
				else:
					sys.exit()
			elif r['remaining'] < 11:
				print "\n\n**WARNING:", r['remaining'], "queries remaining.**"
				print "Current time:",strftime('%I:%M:%S')
				print "Reset time:  ",strftime('%I:%M:%S',localtime(r['reset']))
				print ""
				print "\n\n"
				sleep(10)
		
		#Adding a catch for various Twitter errors
		errors = 0
		while (errors < MAXERRORS):
			try:
				if (firsthit == float("+inf")):
					res = tsearch.search.tweets(q=term+'+-rt',geocode=geocodestr,count=str(tweetspersearch),result_type="recent")
					#pprint(res['statuses'][99])
				else:
					#print 'Test:', term+'+-rt',geocodestr,str(tweetspersearch),str(firsthit)
					res = tsearch.search.tweets(q=term+'+-rt',geocode=geocodestr,count=str(tweetspersearch),result_type="recent",max_id=str(firsthit))
					#pprint(res['statuses'][99])
				break
			except TwitterHTTPError as e:
				errors = errors + 1
				print "Twitter Error encountered. Retrying",MAXERRORS-errors,"more times."                                                       
				print "\n"+e.response_data
				sleep(5)
		if (errors==MAXERRORS):
			print "Repeated errors encountered, possibly due to rate limit."
			print "Will wait 15 minutes and try once more before quitting."
			sleep(900)
			try:
				if (firsthit == float("+inf")):
					res = tsearch.search.tweets(q=term+'+-rt',geocode=geocodestr,count=str(tweetspersearch),result_type="recent")
				else:
					res = tsearch.search.tweets(q=term+'+-rt',geocode=geocodestr,count=str(tweetspersearch),result_type="recent",max_id=str(firsthit))
			except:			
				raise Exception("Gave up because of repeated errors, sorry.")
		res = res['statuses']
			
		print len(res), 'hits on page', startat+pagenum+1, '(max_id='+str(firsthit)+')'
		print r['remaining']-1, 'queries remaining.'
		if (len(res)==0):
			print 'Out of tweets at this location.'
			#print 'Test:', term+'+-rt',geocodestr,str(tweetspersearch),str(firsthit)
			#sleep(1)
			#res = tsearch.search.tweets(q=term+'+-rt',geocode=geocodestr,count=str(tweetspersearch),result_type="recent",max_id=str(firsthit))
			#pprint(res['statuses'][99])
			break
		for i in range(0,len(res)):
			tweetcount = tweetcount + 1
			[outline,outcome,tid,tline] = extractinfo(res[i],wff,raw)
			if outline:
				if not multiloc:
					wf.write(outline)
				elif newmultiloc:
					currloctweets.append([outline[:-1]+','+str(locnum)+'\n',locnum,long(tid)])
					tidbycurrloc.append(float(tid))
					#wf.write(outline[:-1]+','+str(locnum)+'\n')
				elif importmultiloc:
					currloctweets.append([outline[:-1]+','+str(tids[pagenum]+1)+','+str(incls[pagenum])+','+str(locnum)+'\n',locnum,long(tid)])
					tidbycurrloc.append(float(tid))
			if keeptweets:
				#wft.write(tline.encode('ascii','ignore'))
				if not raw:
					wft.write(tline.encode('ascii','ignore'))
				if raw:
					wft.write(tline.encode('ascii','replace'))		#maybe create a separate .utweets file with the Unicode versions of tweets
			outcomes[outcome] = outcomes.get(outcome,0)+1
			if importcsv:
				firsthit = tids[pagenum+1]
			else:
				if firsthit > long(tid):			#if current tweet came before previous oldest, update oldest
					firsthit = long(tid)-1
		if importmultiloc:
			if len(tidbycurrloc) > 0:
				maxtids[pagenum].append(max(tidbycurrloc))
				mintids[pagenum].append(min(tidbycurrloc))
			else:
				maxtids[pagenum].append(0)
				mintids[pagenum].append(0)				
			tweetlist[pagenum].append(currloctweets)
	#endfor searches within a location
	if newmultiloc:
		if len(tidbycurrloc) > 0:
			maxtids[locnum] = max(tidbycurrloc)
			mintids[locnum] = min(tidbycurrloc)
		else:
			maxtids[locnum] = 0
			mintids[locnum] = 0
		searchesleft[locnum] = maxpages-pagenum-1			#calculating how many pages were left in the most maxed-out search
		tweetlist[locnum] = currloctweets
	overwrite = 'a+'
	header = False
	if importcsv:
		firsthit = tids[0]
	else:
		firsthit = float("+inf")

#Endfor multiple locations
if newmultiloc:
	balanceandprint(tweetlist,mintids,maxtids,searchesleft,wf)
elif importmultiloc:
	for pagenum in range(0,maxpages):
		balanceandprint(tweetlist[pagenum],mintids[pagenum],maxtids[pagenum],[0]*len(loclist),wf)
wf.close()
if keeptweets:
	wft.close()
if trackfails:
	wff.close()
	
print '---'
print 'Searched for', term1
print tweetcount, 'tweets found. Centered at ', geocodestr
print 'Locations:', outcomes
print '---'

print 'Queries remaining:',r['remaining']
print "Current time:",strftime('%I:%M:%S')
print "Reset time:  ",strftime('%I:%M:%S',localtime(r['reset']))

