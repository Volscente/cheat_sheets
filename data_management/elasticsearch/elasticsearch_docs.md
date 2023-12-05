# Bugs
## Max Virtual Memory is Too Low
**Error Message:**
```
{"@timestamp":"2023-12-05T21:10:11.581Z", "log.level":"ERROR", "message":"node validation exception\n[1] bootstrap checks failed. You must address the points described in the following [1] lines before starting Elasticsearch. For more information see [https://www.elastic.co/guide/en/elasticsearch/reference/8.11/bootstrap-checks.html]\nbootstrap check failure [1] of [1]: max virtual memory areas vm.max_map_count [65530] is too low, increase to at least [262144]; for more information see [https://www.elastic.co/guide/en/elasticsearch/reference/8.11/_maximum_map_count_check.html]", "ecs.version": "1.2.0","service.name":"ES_ECS","event.dataset":"elasticsearch.server","process.thread.name":"main","log.logger":"org.elasticsearch.bootstrap.Elasticsearch","elasticsearch.node.name":"5e2bb0864007","elasticsearch.cluster.name":"docker-cluster"}

```
**Resolution:**
1. `sudo nano /etc/sysctl.conf`
2. Add the line `kern.maxprocperuid=4096` (Change for the future)
3. Run the command `sudo sysctl -w kern.maxprocperuid=4096
` (Change now)
4. Run docker ES through the following command:
```bash
docker run --name es01 --net elastic_network -p 9200:9200 -it -m 1GB \
  -e "discovery.type=single-node" \
  -e "ES_JAVA_OPTS=-Xms512m -Xmx512m" \
  --ulimit memlock=-1:-1 \
  --ulimit nofile=65536:65536 \
  docker.elastic.co/elasticsearch/elasticsearch:8.11.1

```
