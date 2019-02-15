import matplotlib.pyplot as plt
data = [0.0007, 0.0002, 0.0005, -0.0007, 0.0003, 0.0003, 0.0005, 0.0000, 0.0000, 0.0002, -0.0008, 0.0001, 0.0003, -0.0007, 0.0002, 0.0001, -0.0009, -0.0001, 0.0001, 0.0001, 0.0001, -0.0002, 0.0001, 0.0023, -0.0004, 0.0004, -0.0008, 0.0003, -0.0009, 0.0002]
plt.hist(data, bins = 10, range = (-0.001,0.001), label = "Residual in the Diameter")
plt.xlabel("Residual in cm")
plt.ylabel("Quantity of residuals")
plt.title("Fig. 6: Histogram of Residuals in the Measured Diamater")
plt.legend()
plt.show();
