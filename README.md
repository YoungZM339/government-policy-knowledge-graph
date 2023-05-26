# 政靠“谱”:基于图嵌入的政策智能知识图谱推荐系统

## 部署步骤

- 安装依赖:pip install -r requirements.txt
- 下载并安装neo4j:[Neo4j](https://neo4j.com/download/)
- 创建Neo4j数据库:数据库名称neo4j,用户名neo4j,密码12345678,你也可以在neo4j_db/config.py修改对应配置
- 初始化Neo4j数据库:在项目根目录执行python ./neo4j_db/init_graph.py,这将会从raw_data/中各个文件导入对象、对象各个属性和关系
- 启动Django:python manage.py runserver