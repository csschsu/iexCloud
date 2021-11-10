IEXHOME=/home/christer/iexCloud
mkdir ${IEXHOME}/data 2>/dev/null
cd ${IEXHOME}/src
${IEXHOME}/src/timeSeriesClient.py > ${IEXHOME}/out.log
