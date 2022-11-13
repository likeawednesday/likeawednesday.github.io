# Assignment: Housing II
# Name: Howland, Erin
# Date: 2021-04-18



# Set the working directory to the root of your DSC 520 directory
setwd("c:/GitHub/DSC520")

# Load the from American Community Survey Exercise
housing <- read.csv("Housing.csv")
str(housing)


# Using the dplyr package, use the 6 different operations to analyze/transform the data
# Remember this isn't just modifying data, you are learning about your data also
#   play around and start to understand your dataset in more detail
library(dplyr)

# Mutate
# Select
# Arrange
mutated <- housing %>% select(1, 2, 8, 14:19, 21, 22) %>% mutate(Price_per_SqFt = Sale.Price / square_feet_total_living)
print(mutated)
arranged <- arrange(mutated, desc(Price_per_SqFt))
print(arranged)
head(arranged, 20)
tail(arranged, n=20)


# Filter
filtered <- filter(arranged, square_feet_total_living > 3000, bedrooms >= 4, sq_ft_lot >= 10000)
print(filtered)

# GroupBy
# Summarize
sumz_data <-filtered %>%
  group_by(year_built) %>%
  summarize(Average_Price = mean(Sale.Price), Avg_Price_per_SqFt = mean(Price_per_SqFt), Houses_Sold = n())
nrow(sumz_data)
print(head(sumz_data, 20))
print(tail(sumz_data, 20))


# Using the purrr package - perform 2 functions on your dataset
# You could use zip_n, keep, discard, compact, etc.
library(purrr)
compact(housing$sale_warning)
housing$Sale.Price %>% map(sum)


# Use the cbind and rbind function on your dataset
# total_bath recycled from my last week's code but modified for mutated

# cbind
total_bath <- mutated$bath_full_count + mutated$bath_3qtr_count + mutated$bath_half_count
mutated <- cbind(mutated, total_bath)
head(mutated)

# rbind
new_sales <- c(2019, 846275, 52, 12)
new_sumz <- rbind(sumz_data, new_sales)
print(new_sumz)
head(new_sumz, 20)
tail(new_sumz, 20)


# Split a string
# Then concatenate the results back together
library(stringr)
address <- str_split(housing$addr_full, pattern = " ")
head(address)

address_mat <- data.frame(Reduce(rbind, address))
print(address_mat)

house_num <- address_mat$X1
print(house_num)

street_ad <- paste(address_mat$X1, " ", address_mat$X2, " ",address_mat$X3, " ", address_mat$X4)
print(street_ad)
