import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

# 변환 행렬
A = np.array([[0.25, 0.75],
              [1,    0.5]])

# 플롯 설정
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.grid()

# 초기 벡터 (x, y)와 변환된 벡터 (Ax, Ay)
quiver_x = ax.quiver(0, 0, 1, 0, angles='xy', scale_units='xy', scale=1, color='r')
quiver_y = ax.quiver(0, 0, 0, 1, angles='xy', scale_units='xy', scale=1, color='b')

Ax_initial = A.dot(np.array([1, 0]))
Ay_initial = A.dot(np.array([0, 1]))
quiver_Ax = ax.quiver(0, 0, Ax_initial[0], Ax_initial[1],
                      angles='xy', scale_units='xy', scale=1, color='r', alpha=0.5)
quiver_Ay = ax.quiver(0, 0, Ay_initial[0], Ay_initial[1],
                      angles='xy', scale_units='xy', scale=1, color='b', alpha=0.5)

# 궤적 선(Line2D 객체) 생성
line_x, = ax.plot([], [], 'r-', lw=1)     # x 벡터 궤적 (실선)
line_y, = ax.plot([], [], 'b-', lw=1)     # y 벡터 궤적 (실선)
line_Ax, = ax.plot([], [], 'r--', lw=1)    # Ax 벡터 궤적 (점선)
line_Ay, = ax.plot([], [], 'b--', lw=1)    # Ay 벡터 궤적 (점선)

# 궤적 데이터를 저장할 리스트 초기화
x_traj_x, x_traj_y = [], []
y_traj_x, y_traj_y = [], []
Ax_traj_x, Ax_traj_y = [], []
Ay_traj_x, Ay_traj_y = [], []

total_frames = 100
pause_threshold = 1e-2  # Ax와 Ay가 직교하는지 판별할 임계값
pause_flag = False      # 이미 pause한 상태인지 확인

def update(frame):
    global pause_flag
    
    theta = 2 * np.pi * frame / total_frames
    # x 벡터: (cosθ, sinθ)
    x = np.array([np.cos(theta), np.sin(theta)])
    # y 벡터: x에 대해 90도 회전한 벡터 (-sinθ, cosθ)
    y = np.array([-np.sin(theta), np.cos(theta)])
    
    # 변환된 벡터 계산
    Ax = A.dot(x)
    Ay = A.dot(y)
    
    # Ax와 Ay의 내적 계산 (직교면 0에 가까워짐)
    dot = np.dot(Ax, Ay)
    if np.abs(dot) < pause_threshold and not pause_flag:
        pause_flag = True
        time.sleep(1)  # Ax와 Ay가 직교하는 순간 1초간 멈춤
    if np.abs(dot) >= pause_threshold:
        pause_flag = False
        
    # quiver 객체 업데이트
    quiver_x.set_UVC(x[0], x[1])
    quiver_y.set_UVC(y[0], y[1])
    quiver_Ax.set_UVC(Ax[0], Ax[1])
    quiver_Ay.set_UVC(Ay[0], Ay[1])
    
    # 각 벡터의 tip 좌표를 궤적 리스트에 추가
    x_traj_x.append(x[0])
    x_traj_y.append(x[1])
    y_traj_x.append(y[0])
    y_traj_y.append(y[1])
    Ax_traj_x.append(Ax[0])
    Ax_traj_y.append(Ax[1])
    Ay_traj_x.append(Ay[0])
    Ay_traj_y.append(Ay[1])
    
    # 궤적 선 업데이트
    line_x.set_data(x_traj_x, x_traj_y)
    line_y.set_data(y_traj_x, y_traj_y)
    line_Ax.set_data(Ax_traj_x, Ax_traj_y)
    line_Ay.set_data(Ay_traj_x, Ay_traj_y)
    
    return quiver_x, quiver_y, quiver_Ax, quiver_Ay, line_x, line_y, line_Ax, line_Ay

# blit=False로 설정하여 전체 플롯을 매 프레임마다 다시 그림
ani = animation.FuncAnimation(fig, update, frames=total_frames, interval=50, blit=False)
plt.show()