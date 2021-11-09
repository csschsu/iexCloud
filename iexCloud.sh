IEXHOME=/home/christer/iexCloud
mkdir ${IEXHOME}/datai 2>/dev/null
cd ${IEXHOME}/src
${IEXHOME}/src/timeSeriesClient.py > ${IEXHOME}/out.log