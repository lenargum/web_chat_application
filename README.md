# web_chat_application
IU-F19-DS-Lab10 simple web chat application on sockets with mongo replications

## Report:
### Output of `rs.status()`
```
{
        "set" : "rs0",
        "date" : ISODate("2019-11-01T15:45:14.202Z"),
        "myState" : 1,
        "term" : NumberLong(3),
        "syncingTo" : "",
        "syncSourceHost" : "",
        "syncSourceId" : -1,
        "heartbeatIntervalMillis" : NumberLong(2000),
        "majorityVoteCount" : 2,
        "writeMajorityCount" : 2,
        "optimes" : {
                "lastCommittedOpTime" : {
                        "ts" : Timestamp(1572623110, 1),
                        "t" : NumberLong(3)
                },
                "lastCommittedWallTime" : ISODate("2019-11-01T15:45:10.437Z"),
                "readConcernMajorityOpTime" : {
                        "ts" : Timestamp(1572623110, 1),
                        "t" : NumberLong(3)
                },
                "readConcernMajorityWallTime" : ISODate("2019-11-01T15:45:10.437Z"),
                "appliedOpTime" : {
                        "ts" : Timestamp(1572623110, 1),
                        "t" : NumberLong(3)
                },
                "durableOpTime" : {
                        "ts" : Timestamp(1572623110, 1),
                        "t" : NumberLong(3)
                },
                "lastAppliedWallTime" : ISODate("2019-11-01T15:45:10.437Z"),
                "lastDurableWallTime" : ISODate("2019-11-01T15:45:10.437Z")
        },
        "lastStableRecoveryTimestamp" : Timestamp(1572623070, 1),
        "lastStableCheckpointTimestamp" : Timestamp(1572623070, 1),
        "electionCandidateMetrics" : {
                "lastElectionReason" : "priorityTakeover",
                "lastElectionDate" : ISODate("2019-11-01T13:43:09.890Z"),
                "termAtElection" : NumberLong(3),
                "lastCommittedOpTimeAtElection" : {
                        "ts" : Timestamp(1572615779, 1),
                        "t" : NumberLong(2)
                },
                "lastSeenOpTimeAtElection" : {
                        "ts" : Timestamp(1572615779, 1),
                        "t" : NumberLong(2)
                },
                "numVotesNeeded" : 2,
                "priorityAtElection" : 1,
                "electionTimeoutMillis" : NumberLong(10000),
                "priorPrimaryMemberId" : 1,
                "numCatchUpOps" : NumberLong(1498562884),
                "newTermStartDate" : ISODate("2019-11-01T13:43:10.237Z"),
                "wMajorityWriteAvailabilityDate" : ISODate("2019-11-01T13:43:11.243Z")
        },
        "members" : [
                {
                        "_id" : 0,
                        "name" : "in1:27017",
                        "ip" : "172.31.41.235",
                        "health" : 1,
                        "state" : 1,
                        "stateStr" : "PRIMARY",
                        "uptime" : 8080,
                        "optime" : {
                                "ts" : Timestamp(1572623110, 1),
                                "t" : NumberLong(3)
                        },
                        "optimeDate" : ISODate("2019-11-01T15:45:10Z"),
                        "syncingTo" : "",
                        "syncSourceHost" : "",
                        "syncSourceId" : -1,
                        "infoMessage" : "",
                        "electionTime" : Timestamp(1572615789, 1),
                        "electionDate" : ISODate("2019-11-01T13:43:09Z"),
                        "configVersion" : 2,
                        "self" : true,
                        "lastHeartbeatMessage" : ""
                },
                {
                        "_id" : 1,
                        "name" : "in2:27017",
                        "ip" : "172.31.82.149",
                        "health" : 1,
                        "state" : 2,
                        "stateStr" : "SECONDARY",
                        "uptime" : 6958,
                        "optime" : {
                                "ts" : Timestamp(1572623110, 1),
                                "t" : NumberLong(3)
                        },
                        "optimeDurable" : {
                                "ts" : Timestamp(1572623110, 1),
                                "t" : NumberLong(3)
                        },
                        "optimeDate" : ISODate("2019-11-01T15:45:10Z"),
                        "optimeDurableDate" : ISODate("2019-11-01T15:45:10Z"),
                        "lastHeartbeat" : ISODate("2019-11-01T15:45:13.794Z"),
                        "lastHeartbeatRecv" : ISODate("2019-11-01T15:45:13.064Z"),
                        "pingMs" : NumberLong(1),
                        "lastHeartbeatMessage" : "",
                        "syncingTo" : "in3:27017",
                        "syncSourceHost" : "in3:27017",
                        "syncSourceId" : 2,
                        "infoMessage" : "",
                        "configVersion" : 2
                },
                {
                        "_id" : 2,
                        "name" : "in3:27017",
                        "ip" : "172.31.35.68",
                        "health" : 1,
                        "state" : 2,
                        "stateStr" : "SECONDARY",
                        "uptime" : 6984,
                        "optime" : {
                                "ts" : Timestamp(1572623110, 1),
                                "t" : NumberLong(3)
                        },
                        "optimeDurable" : {
                                "ts" : Timestamp(1572623110, 1),
                                "t" : NumberLong(3)
                        },
                        "optimeDate" : ISODate("2019-11-01T15:45:10Z"),
                        "optimeDurableDate" : ISODate("2019-11-01T15:45:10Z"),
                        "lastHeartbeat" : ISODate("2019-11-01T15:45:13.611Z"),
                        "lastHeartbeatRecv" : ISODate("2019-11-01T15:45:12.974Z"),
                        "pingMs" : NumberLong(0),
                        "lastHeartbeatMessage" : "",
                        "syncingTo" : "in1:27017",
                        "syncSourceHost" : "in1:27017",
                        "syncSourceId" : 0,
                        "infoMessage" : "",
                        "configVersion" : 2
                }
        ],
        "ok" : 1,
        "$clusterTime" : {
                "clusterTime" : Timestamp(1572623110, 1),
                "signature" : {
                        "hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
                        "keyId" : NumberLong(0)
                }
        },
        "operationTime" : Timestamp(1572623110, 1)
}
```

### Output of `rs.config()`
```
{
        "_id" : "rs0",
        "version" : 2,
        "protocolVersion" : NumberLong(1),
        "writeConcernMajorityJournalDefault" : true,
        "members" : [
                {
                        "_id" : 0,
                        "host" : "in1:27017",
                        "arbiterOnly" : false,
                        "buildIndexes" : true,
                        "hidden" : false,
                        "priority" : 1,
                        "tags" : {

                        },
                        "slaveDelay" : NumberLong(0),
                        "votes" : 1
                },
                {
                        "_id" : 1,
                        "host" : "in2:27017",
                        "arbiterOnly" : false,
                        "buildIndexes" : true,
                        "hidden" : false,
                        "priority" : 0.5,
                        "tags" : {

                        },
                        "slaveDelay" : NumberLong(0),
                        "votes" : 1
                },
                {
                        "_id" : 2,
                        "host" : "in3:27017",
                        "arbiterOnly" : false,
                        "buildIndexes" : true,
                        "hidden" : false,
                        "priority" : 0.5,
                        "tags" : {

                        },
                        "slaveDelay" : NumberLong(0),
                        "votes" : 1
                }
        ],
        "settings" : {
                "chainingAllowed" : true,
                "heartbeatIntervalMillis" : 2000,
                "heartbeatTimeoutSecs" : 10,
                "electionTimeoutMillis" : 10000,
                "catchUpTimeoutMillis" : -1,
                "catchUpTakeoverDelayMillis" : 30000,
                "getLastErrorModes" : {

                },
                "getLastErrorDefaults" : {
                        "w" : 1,
                        "wtimeout" : 0
                },
                "replicaSetId" : ObjectId("5db8aa5b05279af727ea6a2c")
        }
}
```

### Screenshot of application with most recent messages
_**before**_ shutting down VPS with primary mongodb instance
![alt text](https://i.imgur.com/AGZwn57.png "Here must be Screenshot 1, but something went wrong :(")

_**after**_ shutting down VPS with primary mongodb instance
![alt text](https://i.imgur.com/sHmVepX.png "Here must be Screenshot 2, but something went wrong :(")
