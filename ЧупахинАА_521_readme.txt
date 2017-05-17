=================================РЕПОЗИТОРИЙ==================================
https://github.com/andxeg/kursovaja_2017


===================================ЗАВИСИМОСТИ=================================
Исходники алгоритма находятся в каталоге ./algo
Для запуска алгоритма понадобится Qt5.



================================ЗАПУСК_АЛГОРИТМА===============================
Для запуска алгоритма нужно выполнить следующие действия:
1. В корневой папке выполнить команду  $ mkdir ./build
2. Далее $ cd ./build
3. Собираем make-файл и компилируем программу $ cmake ../algo && make -j2
4. Запускаем алгоритм $


===============================ИЕРАРХИЯ_КАТАЛОГОВ==============================

./
├── algo
│   ├── CMakeLists.txt
│   ├── common
│   │   ├── CMakeLists.txt
│   │   └── criteria.cpp
│   ├── include
│   │   ├── algorithm.h
│   │   ├── CMakeLists.txt
│   │   ├── computer.cpp
│   │   ├── computer.h
│   │   ├── criteria.h
│   │   ├── defs.h
│   │   ├── edge.h
│   │   ├── element.h
│   │   ├── graph.h
│   │   ├── leafnode.h
│   │   ├── link.cpp
│   │   ├── link.h
│   │   ├── network.h
│   │   ├── node.h
│   │   ├── numa_block.cpp
│   │   ├── numa_block.h
│   │   ├── operation.h
│   │   ├── parameter.h
│   │   ├── path.h
│   │   ├── port.h
│   │   ├── request.h
│   │   ├── serviceAsProvider.h
│   │   ├── serviceAsUser.h
│   │   ├── store.h
│   │   └── switch.h
│   ├── interface
│   │   ├── CMakeLists.txt
│   │   ├── elementfactory.cpp
│   │   ├── elementfactory.h
│   │   ├── export.cpp
│   │   ├── export.h
│   │   ├── factory.cpp
│   │   ├── factory.h
│   │   ├── resourcesxmlfactory.cpp
│   │   ├── resourcesxmlfactory.h
│   │   ├── snapshot.cpp
│   │   ├── snapshot.h
│   │   ├── tenantxmlfactory.cpp
│   │   └── tenantxmlfactory.h
│   ├── main.cpp
│   ├── prototype
│   │   ├── CMakeLists.txt
│   │   ├── exhaustivesearcher.cpp
│   │   ├── exhaustivesearcher.h
│   │   ├── prototype.cpp
│   │   └── prototype.h
│   └── routing
│       ├── bfsqueue.cpp
│       ├── bfsqueue.h
│       ├── bfsrouter.cpp
│       ├── bfsrouter.h
│       ├── bsearcher.cpp
│       ├── bsearcher.h
│       ├── CMakeLists.txt
│       ├── dijkstrarouter.cpp
│       └── dijkstrarouter.h
├── tests
│   ├── input
│   │   ├── A1_NUMA_1.dcxml
│   │   ├── A1_NUMA_2.dcxml
│   │   ├── A1_NUMA_4.dcxml
│   │   ├── A2_NUMA_1.dcxml
│   │   ├── A2_NUMA_2.dcxml
│   │   ├── A2_NUMA_4.dcxml
│   │   ├── A3_NUMA_1.dcxml
│   │   ├── A3_NUMA_2.dcxml
│   │   ├── A3_NUMA_4.dcxml
│   │   ├── A4_NUMA_1.dcxml
│   │   ├── A4_NUMA_2.dcxml
│   │   ├── A4_NUMA_4.dcxml
│   │   ├── A5_NUMA_1.dcxml
│   │   ├── A5_NUMA_2.dcxml
│   │   ├── A5_NUMA_4.dcxml
│   │   ├── policy
│   │   └── rename.sh
│   ├── output
│   │   ├── A1_NUMA_1_result.txt
│   │   ├── A1_NUMA_1_result.xml
│   │   ├── A1_NUMA_2_result.txt
│   │   ├── A1_NUMA_2_result.xml
│   │   ├── A1_NUMA_4_result.txt
│   │   ├── A1_NUMA_4_result.xml
│   │   ├── A2_NUMA_1_result.txt
│   │   ├── A2_NUMA_1_result.xml
│   │   ├── A2_NUMA_2_result.txt
│   │   ├── A2_NUMA_2_result.xml
│   │   ├── A2_NUMA_4_result.txt
│   │   ├── A2_NUMA_4_result.xml
│   │   ├── A3_NUMA_1_result.txt
│   │   ├── A3_NUMA_1_result.xml
│   │   ├── A3_NUMA_2_result.txt
│   │   ├── A3_NUMA_2_result.xml
│   │   ├── A3_NUMA_4_result.txt
│   │   ├── A3_NUMA_4_result.xml
│   │   ├── A4_NUMA_1_result.txt
│   │   ├── A4_NUMA_1_result.xml
│   │   ├── A4_NUMA_2_result.txt
│   │   ├── A4_NUMA_2_result.xml
│   │   ├── A4_NUMA_4_result.txt
│   │   ├── A4_NUMA_4_result.xml
│   │   ├── A5_NUMA_1_result.txt
│   │   ├── A5_NUMA_1_result.xml
│   │   ├── A5_NUMA_2_result.txt
│   │   ├── A5_NUMA_2_result.xml
│   │   ├── A5_NUMA_4_result.txt
│   │   ├── A5_NUMA_4_result.xml
│   │   ├── policy
│   │   └── rename.sh
│   └── tests_result.xls
├── text
│   ├── Курсовая_Работа_16_05_2017.doc
│   └── Курсовая_Работа_16_05_2017.pdf
└── ЧупахинАА_521_readme.txt
