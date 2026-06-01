# 基于强化学习的城市主干路匝道出入口控制

## 1. 研究背景与问题定义

城市主干路出入口是连接城市道路网络与快速路系统的关键过渡节点，具有显著的交通集散与冲突耦合特征。该类区域的运行状态直接影响上游交通组织、下游瓶颈形成以及区域交通诱导策略的有效性。  
本项目围绕“城市主干路匝道出入口交通状态感知—拥挤判别—控制决策”这一完整链条开展研究，目标是在真实交通场景约束下，探索可复现、可迁移的强化学习控制方法。

## 2. 方法框架

研究对象选取为上海市南北高架西线洛川路—共和立交约 150m 匝道出入口场景。整体方法由以下模块构成：

1. **交通流信息提取**：基于无人机视频数据，采用 YOLOv3 模型提取车辆微观运行状态与密度特征。  
2. **交通状态判别**：基于提取特征构建随机森林模型，对拥挤状态进行拟合与识别。  
3. **仿真与控制平台构建**：搭建 TraCI 控制的 SUMO-Python 联合仿真环境，实现真实交通流回放与策略对比实验。  
4. **强化学习控制评估**：设置多种控制策略与无控制基线，评估匝道控制对运行效率指标的影响。

## 3. 主要实验结论

相较无控制方案，强化学习控制策略在目标场景中表现出稳定收益：

- 车道占有率下降约 **14%**；
- 平均车速提升约 **3%**。

上述结果表明，基于强化学习的匝道控制在城市快速路出入口场景中具备一定应用潜力。

## 4. 复现与运行说明

- 上海南北高架洛川路—共和新路立交场景强化学习示例：运行 `SUMO2.py`。  
- 北虹立交交织区信号控制与仿真场景：参见 `beihong-flyover-1` 与 `beihong-flyover-2` 目录。

## 5. 相关扩展研究

在上述研究基础上，我们进一步开展了协同渠化与匝道控制方向的工作。相关成果如下：

```bibtex
@article{deng2023automated,
  title={Automated Traffic State Optimization in the Weaving Area of Urban Expressways by a Reinforcement Learning-Based Cooperative Method of Channelization and Ramp Metering},
  author={Deng, Diantao and Yu, Bo and Xu, Duo and Chen, Yuren and Kong, You and others},
  journal={Journal of Advanced Transportation},
  volume={2023},
  publisher={Hindawi}
}
```

