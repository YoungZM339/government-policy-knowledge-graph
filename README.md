# 政靠“谱”:基于图嵌入的政策智能知识图谱推荐系统

## 部署步骤

- 安装依赖:pip install -r requirements.txt
- 下载并安装neo4j:[Neo4j](https://neo4j.com/download/)
- 创建Neo4j数据库:数据库名称neo4j,用户名neo4j,密码12345678,你也可以在neo4j_db/config.py修改对应配置
- 初始化Neo4j数据库:python neo4j_db/creat_graph.py,这将会从raw_data/relation.txt导入对象和关系
- 启动flask:python app.py

## 关于关系图的前后端配合

首先请看后端发到前端的关系图数据实例:
`
{
    "data": [
        {
            "category": 0,
            "name": "雪雁"
        },
        {
            "category": 0,
            "name": "贾宝玉"
        },
        {
            "category": 0,
            "name": "贾敏"
        },
        {
            "category": 6,
            "name": "林如海"
        },
        {
            "category": 6,
            "name": "林黛玉"
        },
        {
            "category": 5,
            "name": "贾雨村"
        },
        {
            "category": 5,
            "name": "藕官"
        },
        {
            "category": 3,
            "name": "史湘云"
        },
        {
            "category": 5,
            "name": "妙玉"
        },
        {
            "category": 3,
            "name": "贾母"
        }
    ],
    "links": [
        {
            "source": 1,
            "target": 4,
            "value": "表兄妹"
        },
        {
            "source": 7,
            "target": 4,
            "value": "朋友"
        },
        {
            "source": 8,
            "target": 4,
            "value": "朋友"
        },
        {
            "source": 5,
            "target": 4,
            "value": "老师"
        },
        {
            "source": 6,
            "target": 4,
            "value": "丫环"
        },
        {
            "source": 0,
            "target": 4,
            "value": "丫头"
        },
        {
            "source": 9,
            "target": 4,
            "value": "外祖母"
        },
        {
            "source": 2,
            "target": 4,
            "value": "母亲"
        },
        {
            "source": 3,
            "target": 4,
            "value": "父亲"
        },
        {
            "source": 4,
            "target": 1,
            "value": "表兄妹"
        },
        {
            "source": 4,
            "target": 9,
            "value": "外孙女"
        },
        {
            "source": 4,
            "target": 3,
            "value": "女儿"
        }
    ]
}
`

其中，category的值所对应的分类在neo4j_db/config.py中定义，具体为:

`
category_list = {"贾家荣国府": 0, "贾家宁国府": 1, "王家": 2, "史家": 3, "薛家": 4, "其他": 5, "林家": 6}
`

source和target会在后端自动生成。