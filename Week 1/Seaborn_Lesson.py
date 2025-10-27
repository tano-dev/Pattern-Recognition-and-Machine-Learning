import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Import Data & DataSets
# Source: variable = sns.load_dataset('dataset_name')
car_crashes_df = sns.load_dataset('car_crashes')
tips_df = sns.load_dataset('tips')
iris  = sns.load_dataset('iris')
att_df = sns.load_dataset('attention')

# ======================== Matrix Plots ========================
# Heats Map: Biểu đồ nhiệt
# Công dụng: Biểu diễn mối quan hệ giữa các biến số bằng màu sắc (ma trận tương quan).
# Dùng khi: Muốn xem cặp biến nào tương quan cao, thường dùng cho phân tích thống kê ban đầu.
# Source: sns.heatmap(data, annot=True, fmt='fmt_value', cmap='color_map',
#                 center=center_value, vmin=min_value, vmax=max_value,
#                 linewidths=linewidth_value, linecolor='line_color',
#                 cbar=True, cbar_kws={'label': 'colorbar_label'},
#                 square=True, mask=None, xticklabels='auto', yticklabels='auto')

# data: Dữ liệu để vẽ biểu đồ
# annot: Hiển thị giá trị trong ô (True/False)
# fmt: Định dạng giá trị hiển thị trong ô
# cmap: Bản đồ màu sắc để sử dụng
# center: Giá trị trung tâm để căn chỉnh màu sắc
# vmin: Giá trị tối thiểu để hiển thị
# vmax: Giá trị tối đa để hiển thị
# linewidths: Độ dày của đường viền giữa các ô
# linecolor: Màu sắc của đường viền giữa các ô
# cbar: Hiển thị thanh màu sắc (True/False)
# cbar_kws: Tùy chỉnh cho thanh màu sắc (ví dụ: nhãn)
plt.figure(figsize=(10, 8)) 
crash_mx = car_crashes_df.select_dtypes(include='number').corr()    # Tính ma trận tương quan giữa các biến số
sns.heatmap(crash_mx, annot=True)
plt.show()

# Clustermap: Biểu đồ phân cụm
# Công dụng: Phân nhóm dữ liệu dựa trên độ giống nhau, kết hợp heatmap và phân cụm.
# Dùng khi: Làm phân cụm dữ liệu, tìm mối tương đồng giữa các dòng/cột.
# Source: sns.clustermap(data, method='method_name', metric='metric_name',
#                     standard_scale=None, z_score=None, cmap='color_map',
#                     center=center_value, vmin=min_value, vmax=max_value,
#                     annot=True, fmt='fmt_value', linewidths=linewidth_value,
#                     linecolor='line_color', cbar=True, cbar_kws={'label': 'colorbar_label'},
#                     figsize=(width, height), row_cluster=True, col_cluster=True,
#                     row_colors=None, col_colors=None, dendrogram_ratio=(0.2, 0.2),
#                     cbar_pos=None, xticklabels='auto', yticklabels='auto')

# data: Dữ liệu để vẽ biểu đồ
# method: Phương pháp phân cụm (ví dụ: 'single', 'complete', 'average')
# metric: Khoảng cách để tính toán phân cụm (ví dụ: 'euclidean', 'correlation')
# standard_scale: Chuẩn hóa dữ liệu theo hàng hoặc cột (0: hàng, 1: cột)
# z_score: Chuẩn hóa dữ liệu theo z-score (0: hàng, 1: cột)
# cmap: Bản đồ màu sắc để sử dụng
# center: Giá trị trung tâm để căn chỉnh màu sắc
# vmin: Giá trị tối thiểu để hiển thị
# vmax: Giá trị tối đa để hiển thị
# annot: Hiển thị giá trị trong ô (True/False)
# fmt: Định dạng giá trị hiển thị trong ô
# linewidths: Độ dày của đường viền giữa các ô
# linecolor: Màu sắc của đường viền giữa các ô
# cbar: Hiển thị thanh màu sắc (True/False)
# cbar_kws: Tùy chỉnh cho thanh màu sắc (ví dụ: nhãn)
species = iris.pop('species')  # Loại bỏ cột 'species' khỏi DataFrame
sns.clustermap(iris)
plt.show()

# Pair Grids: Biểu đồ lưới cặp
# Công dụng: Trực quan hóa toàn bộ mối quan hệ giữa các cặp biến.
# Dùng khi: Khám phá dữ liệu nhiều chiều, giúp phát hiện xu hướng, phân nhóm.
# Source: sns.PairGrid(data, hue=None, vars=None, x_vars=None, y_vars=None,
#                     diag_sharey=True, aspect=1, height=2.5, palette=None,
#                     dropna=False, corner=False, hue_kws=None, diag_kws=None,
#                     plot_kws=None, diag_sharex=True, sharex=True, sharey=True)

# data: Dữ liệu để vẽ biểu đồ
# hue: Tên cột dữ liệu để phân loại màu sắc
# vars: Danh sách các cột dữ liệu để vẽ biểu đồ
# x_vars: Danh sách các cột dữ liệu để vẽ trục x
# y_vars: Danh sách các cột dữ liệu để vẽ trục y
# diag_sharey: Chia sẻ trục y cho biểu đồ đường chéo (True/False)
# aspect: Tỷ lệ khung hình của mỗi biểu đồ
# height: Chiều cao của mỗi biểu đồ
# palette: Bảng màu sắc để sử dụng
# dropna: Loại bỏ giá trị NaN (True/False)
# corner: Hiển thị chỉ nửa biểu đồ (True/False)
# hue_kws: Tùy chỉnh cho phân loại màu sắc
# diag_kws: Tùy chỉnh cho biểu đồ đường chéo
# plot_kws: Tùy chỉnh cho biểu đồ chính
# diag_sharex: Chia sẻ trục x cho biểu đồ đường chéo (True/False)
# sharex: Chia sẻ trục x cho tất cả các biểu đồ (True/False)
# sharey: Chia sẻ trục y cho tất cả các biểu đồ (True/False)

iriss = sns.load_dataset('iris')  # Tạo bản sao của DataFrame iris
# iris_g = sns.PairGrid(iriss, hue = 'species') # Tạo PairGrid với phân loại theo 'species'
# iris_g.map(plt.scatter)       # Vẽ biểu đồ rải rác cho tất cả các cặp biến
# iris_g.map_diag(plt.hist)     # Vẽ biểu đồ histogram cho đường chéo
# iris_g.map_upper(plt.scatter) # Vẽ biểu đồ rải rác cho nửa trên
# iris_g.map_lower(sns.kdeplot) # Vẽ biểu đồ phân phối cho nửa dưới

iris_g = sns.PairGrid(iriss, hue="species",
                      x_vars = ['sepal_length', 'sepal_width'],
                      y_vars = ['petal_length', 'petal_width'])
iris_g.map(plt.scatter)       # Vẽ biểu đồ rải rác cho các cặp biến
iris_g.add_legend()           # Thêm chú giải cho phân loại màu sắc
plt.show()

# Facet Grids: Biểu đồ lưới mặt
# Công dụng: Hiển thị nhiều biểu đồ nhỏ chia theo phân nhóm.
# Dùng khi: So sánh phân phối theo từng nhóm (giới tính, thời gian, vùng,...)
# Source: sns.FacetGrid(data, col=None, row=None, hue=None, palette=None,
#                     col_wrap=None, height=height_value, aspect=aspect_ratio,
#                     sharex=True, sharey=True, margin_titles=False,
#                     despine=True, dropna=False, legend_out=True,
#                     subplot_kws=None, hue_order=None, col_order=None,
#                     row_order=None, size=None, legend_kws=None)

# data: Dữ liệu để vẽ biểu đồ
# col: Tên cột dữ liệu để phân loại theo cột
# row: Tên cột dữ liệu để phân loại theo hàng
# hue: Tên cột dữ liệu để phân loại màu sắc
# palette: Bảng màu sắc để sử dụng
# col_wrap: Số lượng cột trong mỗi hàng
# height: Chiều cao của mỗi biểu đồ
# aspect: Tỷ lệ khung hình của mỗi biểu đồ
# sharex: Chia sẻ trục x cho tất cả các biểu đồ (True/False)
# sharey: Chia sẻ trục y cho tất cả các biểu đồ (True/False)
# margin_titles: Hiển thị tiêu đề lề (True/False)
# despine: Loại bỏ các đường viền (True/False)
# dropna: Loại bỏ giá trị NaN (True/False)
# legend_out: Hiển thị chú giải bên ngoài lưới (True/False)
# subplot_kws: Tùy chỉnh cho các biểu đồ con
# hue_order: Danh sách các giá trị để sắp xếp phân loại màu sắc
# col_order: Danh sách các giá trị để sắp xếp theo cột
# row_order: Danh sách các giá trị để sắp xếp theo hàng
# size: Kích thước của mỗi biểu đồ
# legend_kws: Tùy chỉnh cho chú giải

# Biểu đồ lưới mặt cho dữ liệu 'tips' với phân loại theo 'time' và 'smoker'
tips_fg = sns.FacetGrid(tips_df, col='time', row='smoker')
tips_fg.map(plt.hist, 'total_bill', bins = 8, edgecolor = 'black' ) # Vẽ biểu đồ histogram cho cột 'total_bill'
plt.show()

# Biểu đồ lưới mặt cho dữ liệu 'tips' với phân loại theo giới tính và người hút thuốc
kws = dict(s=50, linewidth=0.5, edgecolor='black')  # Tùy chỉnh kích thước và đường viền của các điểm dữ liệu
tips_fg = sns.FacetGrid(tips_df, col='sex', hue='smoker', height=4, aspect=1.3,
                        hue_order=['Yes', 'No'],
                        hue_kws=dict(marker=['^', 'v']))  # Tạo lưới mặt với phân loại theo giới tính và người hút thuốc
tips_fg.map(plt.scatter, 'total_bill', 'tip', **kws)  # Vẽ biểu đồ rải rác cho cột 'total_bill' và 'tip'
plt.show()

# Biểu đồ lưới mặt cho dữ liệu 'attention' với phân loại theo 'subject'
att_fg = sns.FacetGrid(att_df, col='subject', col_wrap=5, height=1.5)
att_fg.map(plt.plot, 'solutions', 'score', marker='o')
plt.show()

# ====================== Regression Plots  ======================
# Regression Plots: Biểu đồ hồi quy
# Công dụng: Vẽ biểu đồ phân tán và đường hồi quy tuyến tính.
# Dùng khi: Muốn kiểm tra mối quan hệ tuyến tính giữa 2 biến.

# Source: sns.regplot(x='column_x', y='column_y', data=data, order=order_value,
#                 ci=confidence_interval_value, scatter_kws={'key': 'value'},
#                 line_kws={'key': 'value'}, fit_reg=True, robust=False,
#                 truncate=True, x_estimator=None, x_bins=None, logx=False)
# data: Dữ liệu để vẽ biểu đồ
# x: Tên cột dữ liệu để vẽ trục x
# y: Tên cột dữ liệu để vẽ trục y
# order: Bậc của đa thức hồi quy (mặc định là 1)
# ci: Khoảng tin cậy cho đường hồi quy (mặc định là 95%)
# scatter_kws: Tùy chỉnh cho các điểm dữ liệu (ví dụ: kích thước, màu sắc)
# line_kws: Tùy chỉnh cho đường hồi quy (ví dụ: màu sắc, độ dày)
# fit_reg: Hiển thị đường hồi quy (True/False)
# robust: Sử dụng phương pháp hồi quy mạnh mẽ (True/False)

sns.set_context('paper', font_scale=1.4)
sns.lmplot(x='total_bill', y='tip', data=tips_df, hue='sex', markers=['o', '^'],
           scatter_kws={'s': 100, 'edgecolor': 'w', 'linewidths': 0.5})
plt.show()

# ====================== Categorical Plots ======================
# Categorical Plots: Biểu đồ phân loại

# Bar Plots: Biểu đồ cột
# Công dụng: So sánh trung bình của từng nhóm.
# Dùng khi: Muốn so sánh giá trị trung bình của các nhóm phân loại.

# Source: sns.barplot(x='column_x', y='column_y', data=data, hue='hue_column', estimator=estimator_func)
# data: Dữ liệu để vẽ biểu đồ
# x: Tên cột dữ liệu để vẽ trục x
# y: Tên cột dữ liệu để vẽ trục y
# hue: Tên cột dữ liệu để phân loại màu sắc
# estimator: Hàm ước lượng để tính toán giá trị trung bình (mặc định là mean)
sns.barplot(x='sex', y='total_bill', data=tips_df)
plt.show()

# Count Plots: Biểu đồ đếm
# Công dụng : Đếm số lượng của từng nhóm.
# Dùng khi: Muốn xem số lượng các nhóm phân loại.

# Source: sns.countplot(x='column_name', data=data, hue='hue_column', order=order_list)
# data: Dữ liệu để vẽ biểu đồ
# x: Tên cột dữ liệu để vẽ trục x
# hue: Tên cột dữ liệu để phân loại màu sắc
# order: Danh sách các giá trị để sắp xếp trục x
sns.countplot(x='sex', data=tips_df)
plt.show()

# Violin Plots: Biểu đồ violin
# Công dụng: Hiển thị phân phối, mật độ, trung vị.
# Dùng khi: Muốn xem phân phối của các nhóm phân loại.

# Source: sns.violinplot(x='column_x', y='column_y', data=data, hue='hue_column',
#                     order=order_list, palette='palette_name', width=width_value)
# data: Dữ liệu để vẽ biểu đồ
# x: Tên cột dữ liệu để vẽ trục x
# y: Tên cột dữ liệu để vẽ trục y
# hue: Tên cột dữ liệu để phân loại màu sắc
# order: Danh sách các giá trị để sắp xếp trục x
# palette: Bảng màu sắc để sử dụng
# width: Chiều rộng của biểu đồ
sns.violinplot(x='day', y='total_bill', data=tips_df, hue='sex')
plt.show()

# Strip Plots: Biểu đồ đường
# Công dụng: Biểu diễn phân phối rời rạc.
# Dùng khi: Muốn xem phân phối của các nhóm phân loại với độ nhiễu.

# Source: sns.stripplot(x='column_x', y='column_y', data=data, hue='hue_column',
#                     order=order_list, palette='palette_name', jitter=True, dodge=True)
# data: Dữ liệu để vẽ biểu đồ
# x: Tên cột dữ liệu để vẽ trục x
# y: Tên cột dữ liệu để vẽ trục y
# hue: Tên cột dữ liệu để phân loại màu sắc
# order: Danh sách các giá trị để sắp xếp trục x
# palette: Bảng màu sắc để sử dụng
# jitter: Thêm độ nhiễu vào các điểm dữ liệu (True/False)
# dodge: Tách biệt các điểm dữ liệu theo phân loại (True/False)
plt.figure(figsize=(10, 6))
sns.stripplot(x='day', y='total_bill', data=tips_df, hue='sex', dodge=True)
plt.show()

# Box Plots: Biểu đồ hộp
# Công dụng: Xác định outlier, tứ phân vị.
# Dùng khi: Muốn xem phân phối và outlier của các nhóm phân loại.

# Source: sns.boxplot(x='column_x', y='column_y', data=data, hue='hue_column',
#                 order=order_list, palette='palette_name', width=width_value)
# data: Dữ liệu để vẽ biểu đồ
# x: Tên cột dữ liệu để vẽ trục x
# y: Tên cột dữ liệu để vẽ trục y
# hue: Tên cột dữ liệu để phân loại màu sắc
# order: Danh sách các giá trị để sắp xếp trục x
# palette: Bảng màu sắc để sử dụng
# width: Chiều rộng của biểu đồ
sns.boxplot(x='day', y='total_bill', data=tips_df, hue='sex')
sns.swarmplot(x='day', y='total_bill', data=tips_df, hue='sex', color='white', dodge=True)
plt.show()

# Swarm Plots: Biểu đồ đàn ong
# Công dụng: Hiển thị phân phối rời rạc với độ nhiễu. 
# Dùng khi: Muốn xem phân phối của các nhóm phân loại mà không bị chồng lấn.

# Source: sns.swarmplot(x='column_x', y='column_y', data=data, hue='hue_column',
#                     order=order_list, palette='palette_name', size=size_value)
# data: Dữ liệu để vẽ biểu đồ
# x: Tên cột dữ liệu để vẽ trục x
# y: Tên cột dữ liệu để vẽ trục y
# hue: Tên cột dữ liệu để phân loại màu sắc
# order: Danh sách các giá trị để sắp xếp trục x
# palette: Bảng màu sắc để sử dụng
# size: Kích thước của các điểm dữ liệu
sns.violinplot(x='day', y='total_bill', data=tips_df, hue='sex')
sns.swarmplot(x='day', y='total_bill', data=tips_df, hue='sex', color='black', dodge= True)
plt.show()

# Pallets Plots: Biểu đồ bảng màu
# Source: sns.palplot(palette_name)

# ====================== Distribution Plots ======================
# Distribution Plots: Biểu đồ phân phối
# Công dụng: Vẽ histogram và/hoặc đường KDE
# Dùng khi: Muốn xem phân phối của một biến số.
# Source: sns.displot(data, x='column_name', kde=True, bins=number_of_bins, 
#                     height=height_value, aspect=aspect_ratio, hue='hue_column', 
#                     multiple='stack', col='column_name', row='column_name')

# data: Dữ liệu để vẽ biểu đồ
# x: Tên cột dữ liệu để vẽ trục x
# kde: Hiển thị đường phân phối (True/False)
# bins: Số lượng cột trong biểu đồ
# height: Chiều cao của biểu đồ
# aspect: Tỷ lệ khung hình của biểu đồ
# hue: Tên cột dữ liệu để phân loại màu sắc
# multiple: Cách hiển thị các phân loại (stack, layer, dodge)
# col: Tên cột dữ liệu để phân loại theo cột
# row: Tên cột dữ liệu để phân loại theo hàng
sns.displot(car_crashes_df['not_distracted'], kde=True, bins=30)
plt.show()

# Joint Plots: Biểu đồ kết hợp
# Công dụng: Kết hợp biểu đồ phân tán + histogram/mật độ lề.
# Dùng khi: Muốn xem cả mối quan hệ giữa 2 biến và phân phối từng biến.
# Source: sns.jointplot(data, x='column_x', y='column_y', kind='kind_of_plot',
#                     height=height_value, ratio=ratio_value, space=space_value,
#                     hue='hue_column', marginal_kws={'bins': number_of_bins})

# data: Dữ liệu để vẽ biểu đồ
# x: Tên cột dữ liệu để vẽ trục x
# y: Tên cột dữ liệu để vẽ trục y
# kind: Loại biểu đồ (scatter, hex, kde, reg etc.): scatter (rải rác), hex (nhiệt ), kde (đường phân phối), reg (hồi quy)
# height: Chiều cao của biểu đồ
# ratio: Tỷ lệ giữa biểu đồ chính và biểu đồ lề
# space: Khoảng cách giữa biểu đồ chính và biểu đồ lề
# hue: Tên cột dữ liệu để phân loại màu sắc
# marginal_kws: Tùy chỉnh biểu đồ lề (ví dụ: số lượng cột)
sns.jointplot(data=car_crashes_df, x='speeding', y='alcohol', kind='reg')
plt.show()

# KDE Plots: Biểu đồ phân phối hai biến
# Công dụng: Vẽ đường mật độ xác suất
# Dùng khi: Muốn xem phân phối của hai biến số cùng một lúc.
# Source: sns.kdeplot(data, x='column_x', y='column_y', fill=True, cmap='color_map',
#                 thresh=threshold_value, levels=number_of_levels, common_norm=True)

# data: Dữ liệu để vẽ biểu đồ
# x: Tên cột dữ liệu để vẽ trục x
# y: Tên cột dữ liệu để vẽ trục y
# fill: Điền màu vào vùng dưới đường phân phối (True/False)
# cmap: Bản đồ màu sắc để sử dụng
# thresh: Ngưỡng để hiển thị đường phân phối
# levels: Số lượng mức độ để hiển thị đường phân phối
sns.kdeplot(data=car_crashes_df, x='speeding', y='alcohol', fill=True, cmap='viridis')
plt.show()

# Pair Plots: Biểu đồ cặp
# Công dụng: Vẽ toàn bộ cặp biến trong DataFrame.
# Dùng khi: Khám phá tổng quan dữ liệu nhiều chiều, phân nhóm tốt với hue.
# Source: sns.pairplot(data, hue=None, vars=None, kind='scatter', diag_kind='auto', 
#                      corner=False, markers=None, palette=None, plot_kws=None, 
#                      diag_kws=None, height=2.5, aspect=1, dropna=False)

# data: Dữ liệu để vẽ biểu đồ
# hue: Tên cột dữ liệu để phân loại màu sắc
# vars: Danh sách các cột dữ liệu để vẽ biểu đồ
# kind: Loại biểu đồ (scatter, reg, kde)
# diag_kind: Loại biểu đồ cho đường chéo (auto, hist, kde)
# corner: Hiển thị chỉ nửa biểu đồ (True/False)
# markers: Ký hiệu để sử dụng trong biểu đồ
# palette: Bảng màu sắc để sử dụng
# plot_kws: Tùy chỉnh cho biểu đồ chính
# diag_kws: Tùy chỉnh cho biểu đồ đường chéo
# height: Chiều cao của mỗi biểu đồ
# aspect: Tỷ lệ khung hình của mỗi biểu đồ
# dropna: Loại bỏ giá trị NaN (True/False)
sns.pairplot(tips_df, hue='sex', kind='scatter', diag_kind='kde', height=2.5) # Vẽ biểu đồ cặp với phân loại theo giới tính
plt.show()

# Rug Plots: Biểu đồ đường rìa
# Công dụng: Hiển thị phân bố dữ liệu dọc trục X
# Dùng khi: Muốn xem phân bố của một biến số mà không cần biểu đồ chính.
# Source: sns.rugplot(data, x='column_name', height=height_value,
#                 ax=None, color='color_value', alpha=alpha_value,
#                 linewidth=linewidth_value, clip_on=True, zorder=1)

# data: Dữ liệu để vẽ biểu đồ
# x: Tên cột dữ liệu để vẽ trục x
# height: Chiều cao của đường rìa
# ax: Trục để vẽ biểu đồ (nếu có)
# color: Màu sắc của đường rìa
# alpha: Độ trong suốt của đường rìa
# linewidth: Độ dày của đường rìa
sns.rugplot(tips_df['tip'], height=0.1, color='blue', alpha=0.5, linewidth=1)
plt.show()

# ====================== Styling and Customization ======================
# Styling and Customization: Tùy chỉnh và phong cách
# Source: sns.set_style('style_name'), sns.set_palette('palette_name'), 
#         sns.set_context('context_name'), sns.despine('top', 'right', 'left', 'bottom')
sns.set_style('whitegrid')  # Thiết lập phong cách biểu đồ
sns.set_palette('pastel')  # Thiết lập bảng màu sắc
sns.set_context('talk')  # Thiết lập ngữ cảnh biểu đồ: paper, notebook, talk, poster
sns.despine(top=True, right=True)  # Loại bỏ các đường viền trên và bên phải

