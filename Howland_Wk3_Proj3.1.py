"""
    DSC510
    Wk3
    Assignment 3.1
    Erin Howland
    20 Dec 2020
"""

# Assignment is the same as last week but with the addition of a step-rate discount.
# I've kept the code from last week and just added a section for the new discount.

# Create pretty Welcome
print("")
print("=========================")
print("======== Welcome ========")
print("=========================")
print("")
# Take user input
companyName = input("Please enter company name: ")
feetOfCableFlt = float(input("Please enter desired feet of fiber optic cable: "))
# Convert fractional input to whole number
feetOfCableFlt = -(-feetOfCableFlt // 1)

# calculate step rate bulk discount
bulkRateStepOne = 100
bulkRateStepTwo = 250
bulkRateStepThree = 500


def linearfootprice():
    # no discount for feet of cable ordered under bulk min
    if feetOfCableFlt < bulkRateStepOne:
        return 0.87
    # bulk discount step 1
    elif feetOfCableFlt < bulkRateStepTwo:
        return 0.80
    # bulk discount step 2
    elif feetOfCableFlt < bulkRateStepThree:
        return 0.70
    # bulk discount step 3
    elif feetOfCableFlt >= bulkRateStepThree:
        return 0.50


# Calculate installation cost
installationCost = feetOfCableFlt * linearfootprice()

# calculate shipping discount (for fun... and profit)
shippingDiscountMin = 50
shippingDiscountMax = 100


def discount():
    # no discount for feet of cable ordered under discount min
    if feetOfCableFlt < shippingDiscountMin:
        return 0
    # discount s & h on orders between min and max
    elif feetOfCableFlt < shippingDiscountMax:
        return 0.2*(feetOfCableFlt-50)
    # no s & h calculated for orders over max
    elif feetOfCableFlt >= shippingDiscountMax:
        return 10


shipping = 10-discount()
total = shipping + installationCost

# Begin Invoice
print("")
print("=========================")
print("======== Invoice ========")
print("=========================")
print("")
print("Bill to: " + companyName)
print("")
print("Linear feet of fiber optic cable ordered: " + str("{:,.0f}".format(feetOfCableFlt)))
print("                           Cost per foot: " + str("${:,.2f}".format(linearfootprice())))
print("                           ----------------------")
print("                           Subtotal:  " + str("${:,.2f}".format(installationCost)))
print("                           S & H :    " + str("${:,.2f}".format(shipping)))
print("                           Total:     " + str("${:,.2f}".format(total)))
