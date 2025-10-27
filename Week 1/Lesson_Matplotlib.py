import numpy as np
import matplotlib.pyplot as plt

# =================================== Plot Customization: Tùy chỉnh biểu đồ ===================================
# Create Title: Tạo tiêu đề
# Source: plt.title("Title", fontsize, fontweight, color)
plt.title("My First Plot", fontsize=14, fontweight='bold', color='blue')
# Create Xlabel: Tạo nhãn trục x
# Source: plt.xlabel("X-axis Label", fontsize, fontweight, color)
plt.xlabel("X-axis Label", fontsize=12, fontweight='bold', color='green')
# Create Ylabel: Tạo nhãn trục y
# Source:  plt.ylabel("Y-axis Label", fontsize, fontweight, color)
plt.ylabel("Y-axis Label", fontsize=12, fontweight='bold', color='green')
# Create grid: Tạo lưới
# Source: plt.grid(True)
plt.grid(True)
# Create xlim and ylim: Tạo giới hạn trục x và y
# Source: plt.xlim(0, 100), plt.ylim(0, 100)
plt.xlim(0, 100)
plt.ylim(0, 100)
# Create xticks and yticks: Tạo các nhãn trục x và y
# Source: plt.xticks(np.arange(0, 101, 10)), plt.yticks(np.arange(0, 101, 10))
plt.xticks(np.arange(0, 101, 10))
plt.yticks(np.arange(0, 101, 10))
# Create Legend: Tạo chú thích
# Source: plt.legend(["Label1", "Label2"])
plt.legend(["Data Points"])

# =================================== Plot Types: Các loại biểu đồ ===================================
# Create a scatter plot:  Tạo biểu đồ phân tán (scatter plot)
# Source: plt.scatter(x, y, c, alpha, edgecolors, s, marker)
# c: Màu sắc của các điểm
# alpha: Độ trong suốt của các điểm
# edgecolors: Màu sắc viền của các điểm
# s: Kích thước của các điểm
# marker: Kiểu đánh dấu của các điểm
x_data = np.random.rand(50) * 100
y_data = np.random.rand(50) * 100
plt.scatter(x_data, y_data, c='red', alpha=0.5, edgecolors='w', s=100, marker = "*")
plt.title("Scatter Plot Example")
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
plt.grid(True)
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.legend(["Data Points"])
plt.show()

# Create a line plot: Tạo biểu đồ đường (line plot)
# Source: plt.plot(x, y, c, alpha, linewidth, linestyle)
# c: Màu sắc của đường
# alpha: Độ trong suốt của đường
# linewidth: Độ dày của đường
# linestyle: Kiểu đường (solid, dashed, dotted, etc.)
years_data = np.array([2015 + i for i in range(11)])
money_data = np.random.randint(1000, 5000, size=11)
plt.plot(years_data, money_data, c='blue', alpha=0.8, linewidth=2, linestyle="--", label='Money Over Years')
plt.title("Line Plot Example")
plt.xlabel("Years")
plt.ylabel("Money")
plt.grid(True)
plt.xlim(2015, 2025)
plt.ylim(0, 5000)
plt.legend(["Money Data"])
plt.show()

# Create a bar plot: Tạo biểu đồ cột (bar plot)
# Source: plt.bar(x, height, width, bottom, align, color, alpha, edgecolor, linewidth)
# x: Danh sách các nhãn cho trục x
# height: Chiều cao của các cột
# width: Chiều rộng của các cột
# bottom: Vị trí bắt đầu của các cột
# align: Căn chỉnh của các cột (center, edge)
# color: Màu sắc của các cột
# alpha: Độ trong suốt của các cột
# edgecolor: Màu sắc viền của các cột
# linewidth: Độ dày viền của các cột
Code_Language = np.array(['Python', 'Java', 'C++', 'JavaScript', 'Ruby', 'PHP', 'Swift', 'Go', 'Kotlin', 'Rust'])
Per_Popularity = np.random.randint(1, 100, size=10)
plt.bar(Code_Language, Per_Popularity, width=0.5, color='green', alpha=0.7, edgecolor='black', linewidth=1, align='center')
plt.title("Bar Plot Example")
plt.xlabel("Programming Languages")
plt.ylabel("Popularity (%)")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()  # Adjust layout to prevent clipping of tick-labels
plt.legend(["Popularity Data"])
plt.show()

# Create a histogram: Tạo biểu đồ tần suất (histogram)
# Source: plt.hist(x, bins, range, density, weights, cumulative, bottom, histtype, align)
# x: Dữ liệu để vẽ histogram
# bins: Số lượng cột trong histogram
# range: Giới hạn của histogram
# density: Nếu True, histogram sẽ được chuẩn hóa để tổng diện tích bằng 1
# weights: Trọng số cho mỗi giá trị
# cumulative: Nếu True, histogram sẽ là tích lũy
# bottom: Vị trí bắt đầu của histogram
# histtype: Kiểu histogram (bar, step, stepfilled)
# align: Căn chỉnh của histogram (left, mid, right)
rain_years = np.array([1983 + i for i in range (20)])
rainfall_data = np.array([338, 340, 390, 400, 418, 452, 455, 460, 470, 470, 482, 498, 500, 522, 526, 554, 558, 565, 584, 728])
plt.hist(rainfall_data, bins = 8, range = (300, 800), edgecolor = "black", color= "blue", histtype = "bar", align = "mid")
plt.xlabel("Rainfall (mm)")
plt.ylabel("Frequency")
plt.xticks(np.arange(300, 801, 100))
plt.yticks(np.arange(0, 8, 1))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.title("Histogram Example")
plt.show()

# Create a Pie Chart: Tạo biểu đồ tròn (pie chart)
# Source: plt.pie(x, explode, labels, colors, autopct, shadow, startangle, radius, counterclock)
# x: Dữ liệu để vẽ biểu đồ tròn
# explode: Tách các phần của biểu đồ tròn
# labels: Nhãn cho các phần của biểu đồ tròn
# colors: Màu sắc cho các phần của biểu đồ tròn
# autopct: Hiển thị phần trăm trên các phần của biểu đồ tròn
# shadow: Nếu True, biểu đồ tròn sẽ có bóng
# startangle: Góc bắt đầu của biểu đồ tròn
# radius: Bán kính của biểu đồ tròn
# counterclock: Nếu True, biểu đồ tròn sẽ vẽ theo chiều ngược kim đồng hồ
Freeze_Team = np.array(["Skirk", "Escoffier", "Furina", "Yelan"])
Dmg_Team = np.array([1200, 300, 600, 500])
explodes = np.zeros(len(Freeze_Team))  
explodes[np.argmax(Dmg_Team)] = 0.1  # Tách phần có giá trị lớn nhất
plt.pie(Dmg_Team, labels=Freeze_Team, explode=explodes , colors=['#ff9999',"#53a0ed",'#99ff99','#ffcc99'],  autopct = "%.2f%%",shadow=True, startangle=90)
plt.axis('equal')  # Đảm bảo biểu đồ tròn là hình tròn
plt.show()

# Create a Box plot: Tạo biểu đồ hộp (box plot)
# Source: plt.boxplot(x, notch, vert, patch_artist, labels, widths)
# x: Dữ liệu để vẽ biểu đồ hộp
# notch: Nếu True, biểu đồ hộp sẽ có notch
# vert: Nếu True, biểu đồ hộp sẽ được vẽ theo chiều dọc
# patch_artist: Nếu True, biểu đồ hộp sẽ được tô màu
# labels: Nhãn cho các phần của biểu đồ hộp
# widths: Chiều rộng của các phần của biểu đồ hộp
plt.figure(figsize=(8, 4))
plt.boxplot(rainfall_data, notch=False, vert=False, patch_artist=True, labels=["Rainfall"], widths=0.5, zorder = 1)
y_scatter = np.random.normal(loc=1, scale=0.05, size=len(rainfall_data))  # jitter quanh y=1
plt.scatter(rainfall_data, y_scatter, color='red', alpha=0.6, edgecolors='k', s=50, zorder = 2)
plt.title("Box Plot Example")
plt.ylabel("Rainfall (mm)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Create a Heatmap: Tạo biểu đồ nhiệt (heatmap)
# Source: plt.imshow(data, cmap, interpolation, aspect, origin, extent)
# data: Dữ liệu để vẽ biểu đồ nhiệt
# cmap: Bảng màu cho biểu đồ nhiệt
# interpolation: Phương pháp nội suy cho biểu đồ nhiệt
# aspect: Tỷ lệ khung hình của biểu đồ nhiệt
# origin: Vị trí gốc của biểu đồ nhiệt
# extent: Giới hạn của biểu đồ nhiệt
data = np.random.rand(10, 10)  # Dữ liệu ngẫu nhiên cho biểu đồ nhiệt
plt.imshow(data, cmap='hot', interpolation='nearest', aspect='auto', origin='lower')
plt.colorbar()  # Hiển thị thanh màu
plt.title("Heatmap Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.xticks(np.arange(10), [f"Col {i}" for i in range(10)])
plt.yticks(np.arange(10), [f"Row {i}" for i in range(10)])
plt.show()

# Multipe Figures: Tạo nhiều biểu đồ trong cùng một cửa sổ
# Source: plt.figure(), plt.subplot(), plt.subplots()
# plt.figure(): Tạo một cửa sổ biểu đồ mới
# plt.subplot(): Tạo một biểu đồ con trong cửa sổ biểu đồ
# plt.subplots(): Tạo nhiều biểu đồ con trong cùng một cửa sổ

# Create a figure with multiple subplots: Tạo một cửa sổ biểu đồ với nhiều biểu đồ con
# Source: plt.subplots(nrows, ncols, figsize)
fig, axs = plt.subplots(2, 2, figsize=(10, 8))  # Tạo 2 hàng và 2 cột
# Scatter plot in the first subplot: Tạo biểu đồ phân tán trong biểu đồ con đầu tiên
axs[0, 0].scatter(x_data, y_data, c='red', alpha=0.5, edgecolors='w', s=100, marker = "*")
axs[0, 0].set_title("Scatter Plot")
axs[0, 0].set_xlabel("X-axis Label")
axs[0, 0].set_ylabel("Y-axis Label")
# Line plot in the second subplot: Tạo biểu đồ đường trong biểu đồ con thứ hai
axs[0, 1].plot(years_data, money_data, c='blue', alpha=0.8, linewidth=2, linestyle="--", label='Money Over Years')
axs[0, 1].set_title("Line Plot")
axs[0, 1].set_xlabel("Years")
axs[0, 1].set_ylabel("Money")
# Bar plot in the third subplot: Tạo biểu đồ cột trong biểu đồ con thứ ba
axs[1, 0].bar(Code_Language, Per_Popularity, width=0.5, color='green', alpha=0.7, edgecolor='black', linewidth=1, align='center')
axs[1, 0].set_title("Bar Plot")
axs[1, 0].set_xlabel("Programming Languages")
axs[1, 0].set_ylabel("Popularity (%)")
# Histogram in the fourth subplot: Tạo biểu đồ tần suất trong biểu đồ con thứ tư
axs[1, 1].hist(rainfall_data, bins=8, range=(300, 800), edgecolor="black", color="blue", histtype="bar", align="mid")
axs[1, 1].set_title("Histogram")
axs[1, 1].set_xlabel("Rainfall (mm)")
axs[1, 1].set_ylabel("Frequency")
# Adjust layout to prevent overlap: Tùy chỉnh bố cục để tránh chồng lấn
plt.tight_layout()
plt.savefig("multiplot_example.png")  # Lưu biểu đồ vào file
plt.show()

# =================================== 3D Plotting: Vẽ biểu đồ 3D ===================================
# Axes 3D: Tạo trục 3D
# Source: ax = plt.axes(projection='3d')
ax = plt.axes(projection='3d')  # Tạo trục 3D
plt.show()

# Create a 3D Scatter: Tạo biểu đồ phân tán 3D
# Source: ax.scatter(x, y, z, c, alpha, linewidth, linestyle, marker)
# ax.scatter(): Vẽ biểu đồ phân tán 3D
# x, y, z: Dữ liệu cho trục x, y và z
# c: Màu sắc của các điểm
# alpha: Độ trong suốt của các điểm
# linewidth: Độ dày của viền các điểm
# linestyle: Kiểu đường viền của các điểm
# marker: Kiểu đánh dấu của các điểm
ax = plt.axes(projection='3d')  # Tạo trục 3D
x_3d = np.random.rand(100) * 10
y_3d = np.random.rand(100) * 10
z_3d = np.random.rand(100) * 10
ax.scatter(x_3d, y_3d, z_3d, c='blue', alpha=0.8, linewidth=2, linestyle='-', marker='o')
ax.set_title("3D Scatter Plot Example")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
plt.show()

# Create a 3D Surface Plot: Tạo biểu đồ bề mặt 3D
# Source: ax.plot_surface(X, Y, Z, cmap, edgecolor)
# ax.plot_surface(): Vẽ bề mặt 3D
# X, Y: Dữ liệu cho trục x và y
# Z: Dữ liệu cho trục z
# cmap: Bảng màu cho bề mặt
# edgecolor: Màu sắc viền của bề mặt
ax = plt.axes(projection='3d')  # Tạo trục 3D
x = np.linspace(-5,5, 100)  # Tạo dữ liệu x từ -5 đến 5
y = np.linspace(0, 1, 100)  # Tạo dữ liệu y từ 0 đến 1
X, Y = np.meshgrid(x, y)  # Tạo lưới từ dữ liệu x và y
z = np.sin(X) * np.cos(Y)  # Tính toán dữ liệu z
ax.plot_surface(X, Y, z, cmap='viridis', edgecolor='black')  # Vẽ bề mặt 3D
ax.set_title("3D Surface Plot Example")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
plt.show()

# Create a 3D Wireframe Plot: Tạo biểu đồ lưới 3D
# Source: ax.plot_wireframe(X, Y, Z, color, linewidth, linestyle)
# ax.plot_wireframe(): Vẽ lưới 3D
# X, Y: Dữ liệu cho trục x và y
# Z: Dữ liệu cho trục z
# color: Màu sắc của lưới
# linewidth: Độ dày của lưới
# linestyle: Kiểu đường của lưới
ax = plt.axes(projection='3d')  # Tạo trục 3D
x = np.linspace(0, 100, 100)  # Tạo dữ liệu x từ 0 đến 100
y = np.linspace(0, 50, 50)  # Tạo dữ liệu y từ 0 đến 50
X, Y = np.meshgrid(x, y)  # Tạo lưới từ dữ liệu x và y
z = np.sin(X) * np.cos(Y)  # Tính toán dữ liệu z
ax.plot_wireframe(X, Y, z, color='green', edgecolor='black', linewidth=0.5, linestyle='-')  # Vẽ lưới 3D
ax.set_title("3D Wireframe Plot Example")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
plt.show()






