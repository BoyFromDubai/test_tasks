Задание:
1. Подготовить Docker-образы ElasticSearch, Kibana, Logstash, Filebeat 6.7.2 и 7.7.0 версий
2. С помощью ansible уметь одной командой разворачивать стек ELKF обоих версий
3. Filebeat:
- собрать логи из файла test.log
- из контейнера filebeat с помощью module: docker
- написать конфиг для 2х output: в файл и в logstash
4. Logstash
- настроить input на прием через порт
- в filter:
- обработать логи из test.log (разделить строку на следующие поля: Time, Priority, Logger, RandomNumber, RandomSymbols, Message)
- из логов контейнера filebeat: убрать лишние поля (log.file.path, prospector.type, docker.container.id, docker.container.image); переименовать: host.name =&gt; host, message =&gt; Message; добавить в tags значение из docker.container.name (убрать соответственно docker.container.name)
- в output логи из test.log отправить в ElasticSearch в индекс test-%Y.%m.%d, а логи файлбита записать в файл logstash-output.log
5. В ElasticSearch подготовить template для индекса test-* для 6.7.2 и 7.7.0 версий.
6. В Kibana:
- сохранить поисковый запрос по индексу test-* за последние 12 часов, где выведены все поля, обработанные в Logstash
- создать визуализацию, в которой указывается кол-во документов для каждого значения поля Priority
- такую же визуализацию, но уже для поля Logger
- создать dashboard, в котором будут содержаться все выше перечисленные запросы и визуализации