l=input("Enter a list: ")
item=l.split()

counts={}
for i in item:
    if i in counts:
        counts[i]+=1
    else:
        counts[i]=1

print(f"Purchase frequency: ")
for key in counts:
    print(f"{key}: {counts[key]}")
print()


most_popular_item=""
max_count=0

for key in counts:
    if counts[key]>max_count:
        max_count=counts[key]
        most_popular_item=key

print(f"Most popular item: {most_popular_item}")
print()


print(f"Purchased once:", end="")
for key in counts:
    if counts[key]==1:
        print(key, end=" ")
print()
print()

sorted_items=sorted(counts.items(), key=lambda x: x[1], reverse=True)

print(f"Sorted by frequncy: ")
for item, count in sorted_items:
    print(f"{item}: {count}")
