# 基于强化学习的城市主干路匝道出入口控制
## 背景
城市主干路出入口是连接城市与区域、城市道路和公路的重要过渡性节点，其具有集散性、开放性、发展性等基本性质。同时，城市出入口道路通行状态是影响交通诱导策略的重要因素。本文针对城市主干路出入口，解决了基于无人机视频的城市出入口交通参数提取与分析，实现了基于车辆密度的通行状态判别，完成了基于智能体强化学习对出入口匝道智能控制方法进行研究。
## 研究结果
本文选取上海市南北高架西线—洛川路-共和立交150m匝道出入口作为背景，从交通流特征提取开始，采用了YOLOv3深度学习算法提取到出入口的交通流信息状态，得到了单个车辆的微观行驶状态以及车辆密度。并且通过随机森林算法对其交通流拥挤状态进行了拟合及其判别。最后构建了基于Traci控制的SUMO-python联合仿真平台，对收集到的交通流信息进行了回放，并且采用了4种不同控制手段以及真实交通流去分析对比。强化学习控制匝道方法相比于无控制方案，其车道占有率能下降14%、平均车速提升了3%。
## 运行
- 上海南北高架洛川路到共和新路立交的强化学习demo请运行SUMO2.py
- 更新了北虹立交的交织区信号控制与仿真模拟


## 进一步研究 Further more research

我们已经有了基于上述的进一步研究，如需了解，请参考下面的我们已经发表的论文。
We have already conducted further research based on the above. To learn more, please refer to our published papers below.

@article{deng2023automated,
  title={Automated Traffic State Optimization in the Weaving Area of Urban Expressways by a Reinforcement Learning-Based Cooperative Method of Channelization and Ramp Metering},
  author={Deng, Diantao and Yu, Bo and Xu, Duo and Chen, Yuren and Kong, You and others},
  journal={Journal of Advanced Transportation},
  volume={2023},
  publisher={Hindawi}
}
