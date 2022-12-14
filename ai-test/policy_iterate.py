import gym
import gym_gridworlds
import random
import time

env=gym.make('Gridworld-v0')

class Learn:
    def __init__(self,grid_mdp):
        #初始化状态值函数
        self.v=dict()
        for state in grid_mdp.observation_space:
            self.v[state]=0
        #初始化策略，这些策略均在状态转移概率矩阵中
        self.pi=dict()
        #random.choice(seq):返回列表、元组、字符串的随机项
        self.pi[1]=random.choice(['e','s'])
        self.pi[2]=random.choice(['e','w'])
        self.pi[3]=random.choice(['w','s','e'])
        self.pi[4]=random.choice(['e','w'])
        self.pi[5]=random.choice(['w','s'])
    #策略迭代函数
    def policy_iterate(self,grid_mdp):
        #迭代100次直到策略不变为止
        for i in range(100):
            #策略评估和策略改善交替进行
            self.policy_evaluate(grid_mdp)
            self.policy_improve(grid_mdp)
    #策略评估：
    def policy_evaluate(self,grid_mdp):
        #迭代1000次计算每个状态的真实状态值函数
        for i in range(1000):
            delta=0.0
            #遍历状态空间
            for state in grid_mdp.states:
                #终止状态不用计算状态值函数（v=0.0）
                if state in grid_mdp.terminate_states:
                    continue
                action=self.pi[state]
                t,s,r=grid_mdp.transform(state,action)
                #if s!=-1:
                new_v=r+grid_mdp.gamma*self.v[s]
                delta+=abs(new_v-self.v[state])
                #更新状态值函数
                self.v[state]=new_v
            if delta < 1e-6:
                break
    #策略改善:遍历动作空间，寻找最优动作
    def policy_improve(self,grid_mdp):
        #在每个状态下采用贪婪策略
        for state in grid_mdp.states:
            #终止状态不用计算状态值函数(v=0.0)和求最优策略
            if state in grid_mdp.terminate_states:
                continue
            #假设当前策略为最优动作
            a1=self.pi[state]
            t,s,r=grid_mdp.transform(state,a1)
            #当不在状态转移概率中时，状态动作值函数不存在，状态值函数不变
            #if s!=-1:
            #当前策略下最优状态动作值函数为最优状态值函数
            v1=r+grid_mdp.gamma*self.v[s]
            #遍历动作空间与最优动作进行比较，从而找到最优动作
            for action in grid_mdp.actions:
                #当不在状态转移概率中时，状态动作值函数不存在，状态值函数不变
                t,s,r=grid_mdp.transform(state,action)
                if s!=-1:
                    if v1 < r+grid_mdp.gamma*self.v[s]:
                        a1=action
                        v1=r+grid_mdp.gamma*self.v[s]
            #更新策略
            self.pi[state]=a1
    #最优动作
    def action(self,state):
        return self.pi[state]

gm=env.env
#初始化智能体的状态
state=env.reset()
#实例化对象，获得初始化状态值函数和初始化策略
learn=Learn(gm)
#策略评估和策略改善
learn.policy_iterate(gm)
total_reward=0
#最多走100步到达终止状态
for i in range(100):
    env.render()
    #每个状态的策略都是最优策略
    action=learn.action(state)
    #每一步按照最优策略走
    state,reward,done,_=env.step(action)
    total_reward+=reward
    time.sleep(5)
    if done:
        #显示环境中物体进入终止状态的图像
        env.render()
        break



