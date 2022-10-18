OUT_DIR=/hw/output

hdfs dfs -rm -r -skipTrash $OUT_DIR

(hadoop jar /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar \
-file mapper_1.py \
-mapper "python3 mapper_1.py" \
-file reducer_1.py \
-reducer "python3 reducer_1.py" \
-input /hw/input/AB_NYC_2019.csv \
-output $OUT_DIR)

hdfs dfs -cat $OUT_DIR/part-00000