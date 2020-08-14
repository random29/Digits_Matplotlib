import numpy as np
import pylab
import matplotlib.pyplot as plt
import json
import matplotlib.animation as animation

plt.rcParams['animation.ffmpeg_path'] = 'ffmpeg.exe'
f = open('digits.json', 'r')
digits = json.load(f)
f.close()
fig = plt.figure(figsize=(15, 15))

ims = []


def betweenDigits(digits, number):
    if number == 0:
        control_points_coords_1 = digits['digit_0']['segment_0']
        control_points_coords_2 = digits['digit_0']['segment_1']
        control_points_coords_3 = digits['digit_0']['segment_2']
        control_points_coords_4 = digits['digit_0']['segment_3']
        h_control_points_coords_1 = digits['digit_1']['segment_0']
        h_control_points_coords_2 = digits['digit_1']['segment_1']
        h_control_points_coords_3 = digits['digit_1']['segment_2']
        h_control_points_coords_4 = digits['digit_1']['segment_3']
    elif number == 1:
        control_points_coords_1 = digits['digit_1']['segment_0']
        control_points_coords_2 = digits['digit_1']['segment_1']
        control_points_coords_3 = digits['digit_1']['segment_2']
        control_points_coords_4 = digits['digit_1']['segment_3']
        h_control_points_coords_1 = digits['digit_2']['segment_0']
        h_control_points_coords_2 = digits['digit_2']['segment_1']
        h_control_points_coords_3 = digits['digit_2']['segment_2']
        h_control_points_coords_4 = digits['digit_2']['segment_3']
    elif number == 2:
        control_points_coords_1 = digits['digit_2']['segment_0']
        control_points_coords_2 = digits['digit_2']['segment_1']
        control_points_coords_3 = digits['digit_2']['segment_2']
        control_points_coords_4 = digits['digit_2']['segment_3']
        h_control_points_coords_1 = digits['digit_3']['segment_0']
        h_control_points_coords_2 = digits['digit_3']['segment_1']
        h_control_points_coords_3 = digits['digit_3']['segment_2']
        h_control_points_coords_4 = digits['digit_3']['segment_3']
    elif number == 3:
        control_points_coords_1 = digits['digit_3']['segment_0']
        control_points_coords_2 = digits['digit_3']['segment_1']
        control_points_coords_3 = digits['digit_3']['segment_2']
        control_points_coords_4 = digits['digit_3']['segment_3']
        h_control_points_coords_1 = digits['digit_4']['segment_0']
        h_control_points_coords_2 = digits['digit_4']['segment_1']
        h_control_points_coords_3 = digits['digit_4']['segment_2']
        h_control_points_coords_4 = digits['digit_4']['segment_3']
    elif number == 4:
        control_points_coords_1 = digits['digit_4']['segment_0']
        control_points_coords_2 = digits['digit_4']['segment_1']
        control_points_coords_3 = digits['digit_4']['segment_2']
        control_points_coords_4 = digits['digit_4']['segment_3']
        h_control_points_coords_1 = digits['digit_5']['segment_0']
        h_control_points_coords_2 = digits['digit_5']['segment_1']
        h_control_points_coords_3 = digits['digit_5']['segment_2']
        h_control_points_coords_4 = digits['digit_5']['segment_3']
    elif number == 5:
        control_points_coords_1 = digits['digit_5']['segment_0']
        control_points_coords_2 = digits['digit_5']['segment_1']
        control_points_coords_3 = digits['digit_5']['segment_2']
        control_points_coords_4 = digits['digit_5']['segment_3']
        h_control_points_coords_1 = digits['digit_6']['segment_0']
        h_control_points_coords_2 = digits['digit_6']['segment_1']
        h_control_points_coords_3 = digits['digit_6']['segment_2']
        h_control_points_coords_4 = digits['digit_6']['segment_3']
    elif number == 6:
        control_points_coords_1 = digits['digit_6']['segment_0']
        control_points_coords_2 = digits['digit_6']['segment_1']
        control_points_coords_3 = digits['digit_6']['segment_2']
        control_points_coords_4 = digits['digit_6']['segment_3']
        h_control_points_coords_1 = digits['digit_7']['segment_0']
        h_control_points_coords_2 = digits['digit_7']['segment_1']
        h_control_points_coords_3 = digits['digit_7']['segment_2']
        h_control_points_coords_4 = digits['digit_7']['segment_3']
    elif number == 7:
        control_points_coords_1 = digits['digit_7']['segment_0']
        control_points_coords_2 = digits['digit_7']['segment_1']
        control_points_coords_3 = digits['digit_7']['segment_2']
        control_points_coords_4 = digits['digit_7']['segment_3']
        h_control_points_coords_1 = digits['digit_8']['segment_0']
        h_control_points_coords_2 = digits['digit_8']['segment_1']
        h_control_points_coords_3 = digits['digit_8']['segment_2']
        h_control_points_coords_4 = digits['digit_8']['segment_3']
    elif number == 8:
        control_points_coords_1 = digits['digit_8']['segment_0']
        control_points_coords_2 = digits['digit_8']['segment_1']
        control_points_coords_3 = digits['digit_8']['segment_2']
        control_points_coords_4 = digits['digit_8']['segment_3']
        h_control_points_coords_1 = digits['digit_9']['segment_0']
        h_control_points_coords_2 = digits['digit_9']['segment_1']
        h_control_points_coords_3 = digits['digit_9']['segment_2']
        h_control_points_coords_4 = digits['digit_9']['segment_3']
    elif number == 9:
        control_points_coords_1 = digits['digit_9']['segment_0']
        control_points_coords_2 = digits['digit_9']['segment_1']
        control_points_coords_3 = digits['digit_9']['segment_2']
        control_points_coords_4 = digits['digit_9']['segment_3']
        h_control_points_coords_1 = digits['digit_0']['segment_0']
        h_control_points_coords_2 = digits['digit_0']['segment_1']
        h_control_points_coords_3 = digits['digit_0']['segment_2']
        h_control_points_coords_4 = digits['digit_0']['segment_3']
    sizeOfInterval = 0
    #img = np.ones((512, 512, 3), dtype=np.uint8)
    # rewrite(control_points_coords_1, control_points_coords_2, control_points_coords_3, control_points_coords_4, img)
    # img = np.rot90(img)
    # img = np.rot90(img)
    # img = np.rot90(img)
    # img = np.flip(img, 1)

    # im = plt.imshow(img, animated=True)
    # ims.append([im])
    y = 0.00
    while (y < 1):
        dot1 = np.array([[1, 1], [1, 1], [1, 1], [1, 1]])
        dot2 = np.array([[1, 1], [1, 1], [1, 1], [1, 1]])
        dot3 = np.array([[1, 1], [1, 1], [1, 1], [1, 1]])
        dot4 = np.array([[1, 1], [1, 1], [1, 1], [1, 1]])

        dot1[0][1] = (1 - y) * control_points_coords_1[0][0] + y * h_control_points_coords_1[0][0];
        dot1[1][1] = (1 - y) * control_points_coords_1[1][0] + y * h_control_points_coords_1[1][0];
        dot1[2][1] = (1 - y) * control_points_coords_1[2][0] + y * h_control_points_coords_1[2][0];
        dot1[3][1] = (1 - y) * control_points_coords_1[3][0] + y * h_control_points_coords_1[3][0];
        dot1[0][0] = (1 - y) * control_points_coords_1[0][1] + y * h_control_points_coords_1[0][1];
        dot1[1][0] = (1 - y) * control_points_coords_1[1][1] + y * h_control_points_coords_1[1][1];
        dot1[2][0] = (1 - y) * control_points_coords_1[2][1] + y * h_control_points_coords_1[2][1];
        dot1[3][0] = (1 - y) * control_points_coords_1[3][1] + y * h_control_points_coords_1[3][1];

        dot2[0][1] = (1 - y) * control_points_coords_2[0][0] + y * h_control_points_coords_2[0][0];
        dot2[1][1] = (1 - y) * control_points_coords_2[1][0] + y * h_control_points_coords_2[1][0];
        dot2[2][1] = (1 - y) * control_points_coords_2[2][0] + y * h_control_points_coords_2[2][0];
        dot2[3][1] = (1 - y) * control_points_coords_2[3][0] + y * h_control_points_coords_2[3][0];
        dot2[0][0] = (1 - y) * control_points_coords_2[0][1] + y * h_control_points_coords_2[0][1];
        dot2[1][0] = (1 - y) * control_points_coords_2[1][1] + y * h_control_points_coords_2[1][1];
        dot2[2][0] = (1 - y) * control_points_coords_2[2][1] + y * h_control_points_coords_2[2][1];
        dot2[3][0] = (1 - y) * control_points_coords_2[3][1] + y * h_control_points_coords_2[3][1];

        dot3[0][1] = (1 - y) * control_points_coords_3[0][0] + y * h_control_points_coords_3[0][0];
        dot3[1][1] = (1 - y) * control_points_coords_3[1][0] + y * h_control_points_coords_3[1][0];
        dot3[2][1] = (1 - y) * control_points_coords_3[2][0] + y * h_control_points_coords_3[2][0];
        dot3[3][1] = (1 - y) * control_points_coords_3[3][0] + y * h_control_points_coords_3[3][0];
        dot3[0][0] = (1 - y) * control_points_coords_3[0][1] + y * h_control_points_coords_3[0][1];
        dot3[1][0] = (1 - y) * control_points_coords_3[1][1] + y * h_control_points_coords_3[1][1];
        dot3[2][0] = (1 - y) * control_points_coords_3[2][1] + y * h_control_points_coords_3[2][1];
        dot3[3][0] = (1 - y) * control_points_coords_3[3][1] + y * h_control_points_coords_3[3][1];

        dot4[0][1] = (1 - y) * control_points_coords_4[0][0] + y * h_control_points_coords_4[0][0];
        dot4[1][1] = (1 - y) * control_points_coords_4[1][0] + y * h_control_points_coords_4[1][0];
        dot4[2][1] = (1 - y) * control_points_coords_4[2][0] + y * h_control_points_coords_4[2][0];
        dot4[3][1] = (1 - y) * control_points_coords_4[3][0] + y * h_control_points_coords_4[3][0];
        dot4[0][0] = (1 - y) * control_points_coords_4[0][1] + y * h_control_points_coords_4[0][1];
        dot4[1][0] = (1 - y) * control_points_coords_4[1][1] + y * h_control_points_coords_4[1][1];
        dot4[2][0] = (1 - y) * control_points_coords_4[2][1] + y * h_control_points_coords_4[2][1];
        dot4[3][0] = (1 - y) * control_points_coords_4[3][1] + y * h_control_points_coords_4[3][1];

        img = np.ones((512, 512 , 3), dtype=np.uint8)
        rewrite(dot1, dot2, dot3, dot4, img)
        img[100][10] = [255,255,255]
        # img = np.rot90(img)
        # img = np.rot90(img)
        # img = np.rot90(img)
        # img = np.flip(img, 1)

        #  plt.gca().invert_yaxis()

        im = plt.imshow(img, animated=True)
        ims.append([im])
        y = y + 1/60


def rewrite(control_points_coords_1, control_points_coords_2, control_points_coords_3, control_points_coords_4, img):
    M = np.array([[-1, 3, -3, 1], [3, -6, 3, 0], [-3, 3, 0, 0], [1, 0, 0, 0]])

    # print(control_points_coords_1)
    t = 0
    x = []
    y = []
    i = 0
    sizeOfInterval = 0
    while t < 1:
        T = np.array([[t * t * t, t * t, t, 1]])
        Bez = np.array([[control_points_coords_1[0][0], control_points_coords_1[0][1]],
                        [control_points_coords_1[1][0], control_points_coords_1[1][1]],
                        [control_points_coords_1[2][0], control_points_coords_1[2][1]],
                        [control_points_coords_1[3][0], control_points_coords_1[3][1]]])
        Res_1 = np.dot(T, M)
        res = Res_1 @ Bez
        t = t + 0.01
        temp = int(res[0][0])
        temp_y = int(res[0][1])
        # print(temp)
        # print(temp_y)
        img[temp, temp_y] = [255, 255, 255]
        x.append(temp)
        y.append(temp_y)
        i = i + 1
        sizeOfInterval = sizeOfInterval + 1
    i = 0
    # while i < x.__len__():
    #   x[i][0][0] = int(x[i][0][0])
    #    i = i + 1
    # x.sort()
    while i < sizeOfInterval - 1:
        det_x = x[i + 1] - x[i]
        det_y = y[i + 1] - y[i]
        # if det_x - det_y > 500:
        #     i = i + 1
        #     continue
        # if det_y - det_x > 500:
        #     i = i + 1
        #     continue
        i = i + 1
        bool_x = 0
        bool_y = 0
        if det_x < 0:
            bool_x = 1
        if det_y < 0:
            bool_y = 1
        if (bool_x > 0):
            det_x = det_x * -1
        if (bool_y > 0):
            det_y = det_y * -1
        swap = det_x < det_y
        if (swap > 0):
            det_x, det_y = det_y, det_x
        error = 0
        y_temp = 0
        for x_temp in range(0, det_x + 1):
            if (2 * error > det_x):
                y_temp = y_temp + 1
                error = error - det_x
            error = error + det_y
            len_x = x_temp
            len_y = y_temp
            if (swap > 0):
                len_x, len_y = len_y, len_x
            if (bool_x > 0):
                len_x = len_x * -1
            if (bool_y > 0):
                len_y = len_y * -1
            img[x[i] + len_x, y[i] + len_y] = np.random.rand(1, 3) * 255

    x_1 = []
    t = 0
    y_1 = []
    sizeOfInterval = 0
    while t < 1:
        T = np.array([[t * t * t, t * t, t, 1]])
        Bez = np.array([[control_points_coords_2[0][0], control_points_coords_2[0][1]],
                        [control_points_coords_2[1][0], control_points_coords_2[1][1]],
                        [control_points_coords_2[2][0], control_points_coords_2[2][1]],
                        [control_points_coords_2[3][0], control_points_coords_2[3][1]]])
        Res_1 = np.dot(T, M)
        res = Res_1 @ Bez
        t = t + 0.01
        temp = int(res[0][0])
        temp_y = int(res[0][1])
        # print(temp)
        # print(temp_y)
        img[temp, temp_y] = [255, 255, 255]
        x_1.append(temp)
        y_1.append(temp_y)
        i = i + 1
        sizeOfInterval = sizeOfInterval + 1
    i = 0
    # while i < x.__len__():
    #   x[i][0][0] = int(x[i][0][0])
    #    i = i + 1
    # x.sort()
    while i < sizeOfInterval - 1:
        det_x = x_1[i + 1] - x_1[i]
        det_y = y_1[i + 1] - y_1[i]
        # if det_x - det_y > 500:
        #     i = i + 1
        #     continue
        # if det_y - det_x > 500:
        #     i = i + 1
        #     continue
        i = i + 1
        bool_x = 0
        bool_y = 0
        if det_x < 0:
            bool_x = 1
        if det_y < 0:
            bool_y = 1
        if (bool_x > 0):
            det_x = det_x * -1
        if (bool_y > 0):
            det_y = det_y * -1
        swap = det_x < det_y
        if (swap > 0):
            det_x, det_y = det_y, det_x
        error = 0
        y_temp = 0
        for x_temp in range(0, det_x + 1):
            if (2 * error > det_x):
                y_temp = y_temp + 1
                error = error - det_x
            error = error + det_y
            len_x = x_temp
            len_y = y_temp
            if (swap > 0):
                len_x, len_y = len_y, len_x
            if (bool_x > 0):
                len_x = len_x * -1
            if (bool_y > 0):
                len_y = len_y * -1
            img[x_1[i] + len_x, y_1[i] + len_y] = np.random.rand(1, 3) * 255

    x_2 = []
    y_2 = []
    t = 0
    sizeOfInterval = 0
    while t < 1:
        T = np.array([[t * t * t, t * t, t, 1]])
        Bez = np.array([[control_points_coords_3[0][0], control_points_coords_3[0][1]],
                        [control_points_coords_3[1][0], control_points_coords_3[1][1]],
                        [control_points_coords_3[2][0], control_points_coords_3[2][1]],
                        [control_points_coords_3[3][0], control_points_coords_3[3][1]]])
        Res_1 = np.dot(T, M)
        res = Res_1 @ Bez
        t = t + 0.01
        temp = int(res[0][0])
        temp_y = int(res[0][1])
        # print(temp)
        # print(temp_y)
        img[temp, temp_y] = [255, 255, 255]
        x_2.append(temp)
        y_2.append(temp_y)
        i = i + 1
        sizeOfInterval = sizeOfInterval + 1
    i = 0
    # while i < x.__len__():
    #   x[i][0][0] = int(x[i][0][0])
    #    i = i + 1
    # x.sort()
    while i < sizeOfInterval - 1:
        det_x = x_2[i + 1] - x_2[i]
        det_y = y_2[i + 1] - y_2[i]
        # if det_x - det_y > 500:
        #     i = i + 1
        #     continue
        # if det_y - det_x > 500:
        #     i = i + 1
        #     continue
        i = i + 1
        bool_x = 0
        bool_y = 0
        if det_x < 0:
            bool_x = 1
        if det_y < 0:
            bool_y = 1
        if (bool_x > 0):
            det_x = det_x * -1
        if (bool_y > 0):
            det_y = det_y * -1
        swap = det_x < det_y
        if (swap > 0):
            det_x, det_y = det_y, det_x
        error = 0
        y_temp = 0
        for x_temp in range(0, det_x + 1):
            if (2 * error > det_x):
                y_temp = y_temp + 1
                error = error - det_x
            error = error + det_y
            len_x = x_temp
            len_y = y_temp
            if (swap > 0):
                len_x, len_y = len_y, len_x
            if (bool_x > 0):
                len_x = len_x * -1
            if (bool_y > 0):
                len_y = len_y * -1
            img[x_2[i] + len_x, y_2[i] + len_y] = np.random.rand(1, 3) * 255

    x_1 = []
    y_1 = []
    sizeOfInterval = 0
    t = 0
    while t < 1:
        T = np.array([[t * t * t, t * t, t, 1]])
        Bez = np.array([[control_points_coords_4[0][0], control_points_coords_4[0][1]],
                        [control_points_coords_4[1][0], control_points_coords_4[1][1]],
                        [control_points_coords_4[2][0], control_points_coords_4[2][1]],
                        [control_points_coords_4[3][0], control_points_coords_4[3][1]]])

        Res_1 = np.dot(T, M)
        res = Res_1 @ Bez
        t = t + 0.01
        temp = int(res[0][0])
        temp_y = int(res[0][1])
        # print(temp)
        # print(temp_y)
        img[temp, temp_y] = [255, 255, 255]
        x_1.append(temp)
        y_1.append(temp_y)
        i = i + 1
        sizeOfInterval = sizeOfInterval + 1
    i = 0
    # while i < x.__len__():
    #   x[i][0][0] = int(x[i][0][0])
    #    i = i + 1
    # x.sort()
    while i < sizeOfInterval - 1:
        det_x = x_1[i + 1] - x_1[i]
        det_y = y_1[i + 1] - y_1[i]
        # if det_x - det_y > 500:
        #     i = i + 1
        #     continue
        # if det_y - det_x > 500:
        #     i = i + 1
        #     continue
        i = i + 1
        bool_x = 0
        bool_y = 0
        if det_x < 0:
            bool_x = 1
        if det_y < 0:
            bool_y = 1
        if (bool_x > 0):
            det_x = det_x * -1
        if (bool_y > 0):
            det_y = det_y * -1
        swap = det_x < det_y
        if (swap > 0):
            det_x, det_y = det_y, det_x
        error = 0
        y_temp = 0
        for x_temp in range(0, det_x + 1):
            if (2 * error > det_x):
                y_temp = y_temp + 1
                error = error - det_x
            error = error + det_y
            len_x = x_temp
            len_y = y_temp
            if (swap > 0):
                len_x, len_y = len_y, len_x
            if (bool_x > 0):
                len_x = len_x * -1
            if (bool_y > 0):
                len_y = len_y * -1
            img[x_1[i] + len_x, y_1[i] + len_y] = np.random.rand(1, 3) * 255






betweenDigits(digits, 0)
betweenDigits(digits, 1)
betweenDigits(digits, 2)
betweenDigits(digits, 3)
betweenDigits(digits, 4)
betweenDigits(digits, 5)
betweenDigits(digits, 6)
betweenDigits(digits, 7)
betweenDigits(digits, 8)
betweenDigits(digits, 9)

'''
rewrite(digits, 0, img)
unrewrite(digits, 0)
unrewrite(digits, 1)
unrewrite(digits, 2)
unrewrite(digits, 3)
unrewrite(digits, 4)
unrewrite(digits, 5)
unrewrite(digits, 6)
unrewrite(digits, 7)
unrewrite(digits, 8)
unrewrite(digits, 9)
'''
q = 0
ani = animation.ArtistAnimation(fig, ims, interval=40, blit=True, repeat_delay=5000)

Writer = animation.writers['ffmpeg']
writer = Writer(fps=60, metadata=dict(artist='Me'), bitrate=1800)

ani.save('dynamic_images.mp4', writer)
ani.save('simple_animation.mp4')
# plt.figure()
# plt.imshow(img)
# plt.show()
# plt.imsave('img.png', img)
