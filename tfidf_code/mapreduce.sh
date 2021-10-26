hadoop jar hadoop-streaming-3.3.1.jar -files mapper1.py,reducer1.py -mapper 'python mapper1.py' -reducer 'python reducer1.py' -input User/Data/User_Data/$1 -output /Data/output1


hadoop jar hadoop-streaming-3.3.1.jar -files mapper2.py,reducer2.py -mapper 'python mapper2.py' -reducer 'python reducer2.py' -input User/Data/output1/ -output /Data/output2

hadoop jar hadoop-streaming-3.3.1.jar -files mapper3.py,reducer3.py -mapper 'python mapper3.py' -reducer 'python reducer3.py' -input User/Data/output2/ -output /Data/output3


hadoop jar hadoop-streaming-3.3.1.jar -files mapper4.py -numReduceTasks 0 -input User/Data/output3/ -output /Data/output4 -mapper 'python mapper4.py'

hdfs dfs -getmerge /Data/output4 tfidf_Results/$1 

hadoop fs -rm -r /Data/output*