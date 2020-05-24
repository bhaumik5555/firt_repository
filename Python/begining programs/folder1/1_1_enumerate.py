months = ["Jan", "Feb", "Mar", "April", "May", "June"]

print({num+1:month for num,month in enumerate(months)})


print({num:month for num in range(1,7) for month in months})

print({num:month for num,month in zip(range(1,7),months)})
