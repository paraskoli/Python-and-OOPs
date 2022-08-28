# for i in range(2,21):
#     with open(f"table/Multiplication_table_of {i}.txt","w") as f:
#         for j in range(1,11):
#                 f.write(f"{i}*{j}={i*j}\n")

# for i in range(1,21):
#     with open(f"table/mult-table-of{i}.txt","w") as f:
#         for j in range(1,11):
#             f.write(f"{i}*{j}={i*j}")
#             if j!=10:
#                 f.write("\n")


for i in range(2,21):
    with open(f"table/table-of {i}.txt","w") as f:
        for j in range(1,11):
            f.write(f"{i}*{j}={i*j}")
            if j!=10:
                f.write("\n")