import pandas as pd 

# ========================= LOAD DATA =========================
# Load the dataset: Đọc dữ liệu từ file CSV: Đọc dữ liệu từ file CSV
# Source: variable = pd.read_csv('Pandas/file_path')
df_csv = pd.read_csv('Pandas/pokemon_data.csv')

# Load the dataset from a text file: Đọc dữ liệu từ file văn bản
# Source: variable = pd.read_csv('Pandas/file_path', delimiter='\t')
df_txt = pd.read_csv('Pandas/pokemon_data.txt', delimiter='\t')

# Load the dataset from an Excel file: Đọc dữ liệu từ file Excel
# Source: variable = pd.read_excel('Pandas/file_path', sheet_name='Sheet1')
df_xlsx = pd.read_excel('Pandas/pokemon_data.xlsx', sheet_name='pokemon_data')

# ========================= SAVE DATA =========================
# Saving Our Data: Lưu dữ liệu 
# Save DataFrame to CSV: Lưu DataFrame vào file CSV
# Source: variable.to_csv('file_path', index=False)
df_csv.to_csv('Pandas/pokemon_data_modified.csv', index=False)  # Save to CSV without index

# Save DataFrame to Excel: Lưu DataFrame vào file Excel
# Source: variable.to_excel('file_path', sheet_name='Sheet1', index=False)
df_csv.to_excel('Pandas/pokemon_data_modified.xlsx', sheet_name='pokemon_data', index=False)  # Save to Excel without index

# Save DataFrame to text file: Lưu DataFrame vào file văn bản
# Source: variable.to_csv('file_path', sep='\t', index=False)
df_csv.to_csv('Pandas/pokemon_data_modified.txt', sep='\t', index=False)  # Save to text file with tab separator

# ========================= DISPLAY DATA =========================
# Display the first and last 10 rows of the DataFrame: Hiển thị 10 dòng đầu và 10 dòng cuối của DataFrame
df_txt.head(10)                                         # Display the first 10 rows
df_csv.tail(10)                                         # Display the last 10 rows
df_csv.sample(10)                                       # Display 10 random rows

# Display the Shape of Data Frame: Hiển thị kích thước của DataFrame
df_xlsx.shape                                           # Display the shape of the DataFrame

# Display the Data Types of each column: Hiển thị kiểu dữ liệu của từng cột
df_csv.dtypes                                           # Display the data types of each column    

# Read header: Đọc tiêu đề của DataFrame
df_csv.columns                                          # Display the header of the DataFrame

# Read Information about DataFrame: Hiển thị thông tin về DataFrame
df_csv.info()                                           # Display information about the DataFrame

# Copy DataFrame: Sao chép DataFrame
df_copy = df_csv.copy()                                 # Create a copy of the DataFrame

# ========================= ACCESS DATA =========================
# Reach each column by name: Đọc từng cột trong DataFrame
# Source: variable['column_name']                       # Access a specific column by name
df_csv['Name']                                          
# Source: variable[['column1', 'column2',...]]          # Access multiple columns by name
df_csv[['Name', 'Type 1']]                              
# Souce: variable.column_name                           # Access a specific column using dot notation
df_csv.Name                     

# ========================= ACCESS SPECIFIC VALUES =========================
# .at: Truy cập giá trị tại chỉ số dòng và tên cột
df_csv.at[0, 'Name']                                    # Giá trị dòng đầu, cột 'Name'

# .iat: Truy cập giá trị tại chỉ số dòng và chỉ số cột
df_csv.iat[0, 1]                                        # Giá trị dòng đầu, cột thứ 2

# ========================= ACCESS ROWS AND COLUMNS =========================
# .iloc: Truy cập dòng theo chỉ số
df_csv.iloc[1]                                          # Dòng thứ 2 (index 1)

# .iloc: Truy cập giá trị tại chỉ số dòng và chỉ số cột
df_csv.iloc[2, 1]                                       # Giá trị dòng 2, cột 1

# .iloc: Truy cập nhiều dòng theo chỉ số
df_csv.iloc[0:5]                                        # Dòng từ 0 đến 4

# .iloc: Truy cập nhiều dòng và cột theo chỉ số
df_csv.iloc[0:5, 1:3]                                   # Dòng 0-4, cột 1-2

# .loc: Truy cập giá trị tại chỉ số dòng và tên cột
df_csv.loc[2, 'Name']                                   # Giá trị dòng 2, cột 'Name'

# .loc: Truy cập nhiều dòng và cột theo tên
df_csv.loc[0:4, ['Name', 'Type 1']]                     # Dòng 0-4, cột 'Name' và 'Type 1'

# ========================= ITERATE =========================
# Iterate through each row: Lấy từng dòng trong DataFrame
# Source: for index, row in variable.iterrows(): Code   
for index, row in df_csv.iterrows():                    # Print each row's index and 'Name' column
    index, row['Name']                                                               

# ========================= FILTER & SORT DATA =========================
# Filter DataFrame by condition: Lọc dữ liệu theo điều kiện
# Source: variable[variable['column_name'] == value]    
df_csv['Name'].loc[df_csv['Type 1'] == 'Bug']

# Filter DataFrame by multiple conditions: Lọc dữ liệu có sử dụng nhiều điều kiện
# Source: variable[(variable['column1'] == value1) & (variable['column2'] == value2) & ...]
df_csv.loc[(df_csv['Type 1'] == 'Fire') & (df_csv['Type 2'] == 'Flying')]

# Sort DataFrame by a specific column: Sắp xếp DataFrame theo một cột cụ thể
# Source: variable.sort_values(by='column_name', ascending=1/0)
df_csv.sort_values(by='Name', ascending = 1)             # Sort by 'Name' in ascending order

# Sort DataFrame by multiple columns: Sắp xếp DataFrame theo nhiều cột
# Source: variable.sort_values(by=['column1', 'column2',....], ascending=[1/ 0, 1/0, ...])
df_csv.sort_values(by=['HP', 'Generation'])              # Sort by 'HP' ascending and 'Generation' ascending

# ========================= DESCRIBE & STRING FILTER =========================
# Describe DataFrame: Mô tả dữ liệu trong DataFrame
# Source: variable.describe()                            
df_csv.describe()                                        # Get a statistical summary of the DataFrame

# Filter DataFrame by string condition: Lọc dữ liệu theo điều kiện chuỗi
# Source: variable[variable['column_name'].str.contains('string')]
df_csv.loc[df_csv['Name'].str.contains('Mega')]          # Filter rows where 'Name' contains 'Mega'

# Split string in a column: Tách chuỗi trong một cột
# Source: variable['column_name'].str.split('separator', expand=True)
df_csv['Name'].str.split(' ', expand=True)              # Split 'Name' by space and expand into multiple columns

# Strip whitespace from string in a column: Loại bỏ khoảng trắng trong chuỗi
# Source: variable['column_name'].str.strip()
df_csv['Name'].str.strip()                               # Remove leading and trailing whitespace from 'Name'

# ========================= MODIFY DATA =========================
# Making change to DataFrame: Thay đổi dữ liệu trong DataFrame
# Add a new column: Thêm một cột mới
# Source: variable['column_name'] = new_value
df_csv['Total'] = df_csv.iloc[:, 4:10].sum(axis=1)      # Calculate the total of specific columns

# Reorder columns: Sắp xếp lại thứ tự các cột
cols = list(df_csv.columns)                             # Get the list of columns  
df_csv = df_csv[cols[0:4] + [cols[-1]] + cols[4:12]]    # Reorder columns

# Remove a column: Xoá một cột
# Source: variable.drop('column_name', axis=1)          # Drop a column
df_csv.drop('Total', axis=1, inplace=True)              # Drop the 'Total' column

# Rename a column: Đổi tên một cột
# Source: variable.rename(columns={'old_name': 'new_name'})
df_csv.rename(columns={'Type 1': 'Primary Type', 'Type 2': 'Secondary Type'}, inplace=True)  # Rename columns

# Reset index: Đặt lại chỉ mục
new_df = df_csv.loc[(df_csv['Primary Type'] == 'Fire') & (df_csv['Secondary Type'] == 'Flying')]  # Filter DataFrame
# Source: variable.reset_index(drop=True)
new_df.reset_index(drop=True, inplace=True)             # Reset the index of the DataFrame

# ========================= CONDITION CHANGES =========================
# Condition Changes : Thay đổi dữ liệu theo điều kiện

# Change values in a column based on condition: Thay đổi giá trị trong cột theo điều kiện
# Source: variable.loc[condition, 'column_name'] = new_value
# df_csv.loc[['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'     # Change 'Type 1' from 'Fire' to 'Flamer'

# ========================= AGGREGATE DATA =========================
# Aggreate data: Tính toán tổng hợp dữ liệu
df = pd.read_csv('Pandas/pokemon_data_modified.csv')    # Load modified data

# Group by a specific column and calculate the mean: Nhóm theo cột và tính trung bình
# Mean values for each group: Tính trung bình giá trị cho mỗi nhóm
# Source: variable.groupby('column_name').mean(numeric_only=True)
type_mean = df.groupby('Type 1').mean(numeric_only=True)
type_mean = type_mean.sort_values(by='HP', ascending=True)

# Sum values for each group: Tính tổng giá trị cho mỗi nhóm
# Source: variable.groupby('column_name').sum(numeric_only=True)
total_type = df.groupby('Type 1').sum(numeric_only=True)  
tottal_type = total_type.sort_values(by='HP', ascending=True)

# Count values for each group: Đếm số lượng giá trị cho mỗi nhóm
# Source: variable.groupby('column_name').count()
df['Count'] = 1
count_type = df.groupby('Type 1').count()['Count']      # Count occurrences of 'Type 1'

# ========================= WORKING WITH LARGE AMOUNTS OF DATA =========================
# Working with large amounts of data: Làm việc với dữ liệu lớn
new_df = pd.DataFrame(columns=df.columns)  

# Load large dataset in chunks: Đọc dữ liệu lớn theo từng phần
# Source: pd.read_csv('file_path', chunksize=chunk_size)
for df in pd.read_csv('Pandas/pokemon_data.csv', chunksize=100):
    result = df.groupby('Type 1').count()
    new_df = pd.concat([new_df, result], ignore_index=True)  # Concatenate results into new DataFrame

# ========================= ADVANCE PROCESSING =========================
# Advance Processing: Xử lý nâng cao
# Missing Values: Xử lý giá trị thiếu
df.isnull().sum()                                    # Count missing values in each column
# Remove rows with missing values: Xoá các dòng có giá trị thiếu
df.dropna(inplace=True)                              # Remove rows with any missing values
# Check for missing values: Kiểm tra giá trị thiếu
df.isnull().values.any()                             # Check if there are any missing values
# Fill missing values: Điền giá trị thiếu
df.fillna(value=0, inplace=True)                     # Fill missing values with 0

# Data Type Conversion: Chuyển đổi kiểu dữ liệu
# Convert column data type: Chuyển đổi kiểu dữ liệu của cột
# Source: variable['column_name'] = variable['column_name'].astype(new_type)
df['HP'] = df['HP'].astype(int)                      # Convert 'HP' column to integer type

# Convert multiple columns data type: Chuyển đổi kiểu dữ liệu của nhiều cột
# Source: variable[['column1', 'column2']] = variable[['column1', 'column2']].astype(new_type)
df[['HP', 'Attack']] = df[['HP', 'Attack']].astype(float)  # Convert 'HP' and 'Attack' columns to float type

# ========================= APPLY & CUSTOM FUNCTIONS =========================
# Applying Functions: Áp dụng hàm
# Using Lambda Functions: Sử dụng hàm Lambda
# Source: variable['new_column'] = variable['column_name'].apply(lambda x: function(x))
df['New Column'] = df['HP'].apply(lambda x: x * 2)   # Apply a function to 'HP' column and create 'New Column'

# Using Custom Functions: Sử dụng hàm tùy chỉnh
# Source: variable['new_column'] = variable['column_name'].apply(function)
def custom_function(x):
    return x + 10      
df['New Column'] = df['HP'].apply(custom_function)   # Apply custom function to 'HP' column and create 'New Column'

# Apply function to each row: Áp dụng hàm cho mỗi dòng
# Source: variable.apply(lambda row: function(row), axis=1)
df.apply(lambda row: row['HP'] + row['Attack'], axis=1)  # Apply function to each row and return sum of 'HP' and 'Attack'

# Filter DataFrame using a custom function: Lọc DataFrame bằng hàm tùy chỉnh
# Source: variable[variable['column_name'].filter(function)]
filtered_df = df[df['HP'].filter(lambda x: x > 50)]

# Duplicated Rows: Xử lý dòng trùng lặp
# Check for duplicated rows: Kiểm tra dòng trùng lặp
# Source: variable[variable.duplicated(keep ='first/last/false') )]
duplicated_rows = df[df.duplicated(keep='first')]  # Get duplicated rows, keeping the first occurrence

# ========================= MERGE & CONCATENATE =========================
# Merging DataFrames: Kết hợp DataFrame
# Merge two DataFrames on a specific column: Kết hợp hai DataFrame theo một cột cụ thể
# Source: variable.merge(other_variable, on='column_name', how='inner/outer/left/right')
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['A', 'B', 'C']})
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Value': [20, 30, 40]})
merged_df = df1.merge(df2, on='ID', how='inner')     # Inner join on 'ID' column

# Concatenate two DataFrames: Nối hai DataFrame
# Source: pd.concat([variable1, variable2], axis=0/1)
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
concatenated_df = pd.concat([df1, df2], axis=0)      # Concatenate vertically (rows)

# ========================= STRING OPERATIONS =========================
# String Operations: Xử lý chuỗi
# Convert string to lowercase: Chuyển đổi chuỗi thành chữ thường
df['Name'] = df['Name'].str.lower()                  # Convert 'Name' column to lowercase
# Convert string to uppercase: Chuyển đổi chuỗi thành chữ hoa
df['Name'] = df['Name'].str.upper()                  # Convert 'Name' column
# Replace substrings in a string: Thay thế chuỗi con trong chuỗi
df['Name'] = df['Name'].str.replace('Pikachu', 'Electric Mouse')  # Replace 'Pikachu' with 'Electric Mouse'

# ========================= STATISTICS & UNIQUES =========================
# Staticstical Operations: Thống kê dữ liệu
df.describe()                                        # Get a statistical summary of the DataFrame

# Count occurrences of a value in a column: Đếm số lần xuất hiện của một giá trị trong cột
# Source: variable['column_name'].value_counts()
df['HP'].value_counts()                              # Count occurrences of each unique value in 'HP' column

## Get unique values in a column: Lấy các giá trị duy nhất trong một cột
# Source: variable['column_name'].unique()
df['HP'].unique()                                    # Get unique values in 'HP' column

# ========================= PIVOT & CROSSTAB =========================
# Pivot Table: Tạo bảng Pivot
# Tạo bảng tổng hợp dữ liệu với các giá trị trung bình của 'HP' cho từng 'Type 1' và từng 'Generation'
# Source: pd.pivot_table(data, values='column', index=['index_column'], columns=['column'], aggfunc='mean')
pivot_table = pd.pivot_table(df, values='HP', index=['Type 1'], columns=['Generation'], aggfunc='mean')

# Crosstab: Tạo bảng chéo
# Đếm số lượng từng loại 'Type 1' theo từng 'Generation'
# Source: pd.crosstab(index=data['column1'], columns=data['column2'])
crosstab = pd.crosstab(df['Type 1'], df['Generation'])

# ========================= TIME SERIES ANALYSIS =========================
# Time Series Analysis: Phân tích chuỗi thời gian
# Convert string to datetime: Chuyển đổi chuỗi thành datetime
# Source: variable['column_name'] = pd.to_datetime(variable['column_name'])
df['Date'] = pd.to_datetime(df['Date'])              # Convert 'Date' column to datetime type

# Extract date components: Trích xuất các thành phần ngày tháng
# Source: variable['column_name'].dt.component { component can be year, month, day, etc.}
df['Date'].dt.year                                   # Extract year from 'Date' column
df['Date'].dt.month                                  # Extract month from 'Date' column  
df['Date'].dt.day                                    # Extract day from 'Date' column

