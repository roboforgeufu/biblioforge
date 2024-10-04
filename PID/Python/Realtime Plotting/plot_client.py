import socket
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Definindo IP do ev3
IPaddress = str("192.168.137.16")

# Conectando ao servidor
s = socket.socket()
s.connect((IPaddress, 12345))

# Criando base do gráfico
plt.style.use("ggplot")
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=[10, 7])

# Criando variáveis
rcvdData = "None"
x_time = []
y1_pid = []
y2_angle = []

V_LIMIT = 200

top_limit = V_LIMIT
bot_limit = -V_LIMIT

new_offset = 0


def animate(i):
    global top_limit
    global bot_limit
    global new_offset

    right_limit_offset = 10000
    left_limit = 0

    rcvdData = s.recv(1024).decode()

    # Recebendo lista de log em forma de string
    if rcvdData != "end":
        # Divide o string em uma lista
        rcvdDatalist = rcvdData.split(",")
        sendData = "received data!"
        s.send(sendData.encode())

        for i, value in enumerate(rcvdDatalist):
            rcvdDatalist[i] = float(value)

        time = rcvdDatalist[0]
        instance = rcvdDatalist[1]
        p_gain = rcvdDatalist[2]
        d_gain = rcvdDatalist[3]
        i_gain = rcvdDatalist[4]
        pid = rcvdDatalist[5]
        angle = rcvdDatalist[6]
        target = rcvdDatalist[7]

        print(
            "Target:",
            target,
            "Angle:",
            angle,
            "P:",
            p_gain,
            "D:",
            d_gain,
            "I:",
            i_gain,
            "PID",
            pid,
        )

        # Limite superior e inferior aumentam com base no PID

        if pid > top_limit:
            top_limit = pid + V_LIMIT
        if pid < bot_limit:
            bot_limit = pid - V_LIMIT

        # Limite da esquerda aumenta se passar de 3 segundos antes do tempo máximo (exceto na última curva (8))
        if time > right_limit_offset - 3000:
            if instance != 8: #não entendi direito o porquê dessa instância
                new_offset = time + 3000
                right_limit = new_offset

            # Limite só aumenta se o gráfico atingir a borda durante a última curva (8)
            else:
                if time > new_offset:
                    new_offset = time
                right_limit = new_offset

        # Limite se mantém em qualquer outra situação
        else:
            right_limit = right_limit_offset

        ax.set_xlim(left_limit, right_limit)
        ax.set_ylim(bot_limit, top_limit)
        x_time.append(time)
        y1_pid.append(pid)
        y2_angle.append(angle)

        ax.plot(
            x_time,
            y1_pid,
            color="blue",
        )
        ax.plot(x_time, y2_angle, color="red")

    # Encerra conexão
    else:
        sendData = "ending process..."
        s.send(sendData.encode())
        s.close()
        sys.exit("Connection ended!")


anim = animation.FuncAnimation(fig, animate, interval=1)
plt.show()
FFwriter = animation.FFMpegWriter(fps=10)
anim.save("pid.mp4", writer=FFwriter)
