FROM apache/hive:4.0.0-alpha-2

USER root

# Install wget (just in case, should be in the base image)
RUN apt-get update && apt-get install -y wget --no-install-recommends && apt-get clean && rm -rf /var/lib/apt/lists/*

# Define versions for JARs as ARGuments - easier to update later
ARG HADOOP_AWS_VERSION=3.3.1
ARG AWS_SDK_BUNDLE_VERSION=1.11.901
ARG HADOOP_COMMON_VERSION=3.3.1 # You might need this for Hive as well, depending on your setup

# Download Hadoop AWS JAR
RUN wget -P /opt/hive/lib "https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/${HADOOP_AWS_VERSION}/hadoop-aws-${HADOOP_AWS_VERSION}.jar"

# Download AWS SDK Bundle JAR
RUN wget -P /opt/hive/lib "https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/${AWS_SDK_BUNDLE_VERSION}/aws-java-sdk-bundle-${AWS_SDK_BUNDLE_VERSION}.jar"

# Download Hadoop Common JAR (if needed for Hive specifically)
RUN wget -P /opt/hive/lib "https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-common/${HADOOP_COMMON_VERSION}/hadoop-common-${HADOOP_COMMON_VERSION}.jar"

# USER hive