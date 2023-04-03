import torch
from torch.autograd import Variable
import numpy as np

class linearRegression(torch.nn.Module):            
    
    # instantiating Linear Regression class
    def __init__(self,ndimsx,ndimsy):
        super(linearRegression, self).__init__() 
        self.lr_pytorch = torch.nn.Linear(ndimsx,ndimsy)                                                       # Linear block in pytorch

    def forward(self,input_to_predict):                                                              # Forward propagation (Prediction)
        predictions = self.lr_pytorch(input_to_predict)
        return predictions
            
    def fit(self,inputs,outputs,epochs = 10, learning_rate = 0.01):                                 # Fit method to train on existing data
        
        inputs = Variable(torch.from_numpy(np.array(inputs,dtype=np.float32)))                      # converting np.array to tensors for operations
        labels = Variable(torch.from_numpy(np.array(outputs,dtype=np.float32).reshape(-1,1))) 
        
        stochastic_gradient_descent = torch.optim.SGD(self.lr_pytorch.parameters(),learning_rate)  # instantiating SGD Gradient Descent 
        mse_loss_function = torch.nn.MSELoss()                                                      # Instantiationg MSE Loss function
        
        for epoch in range(epochs):                                                                 # Training 
            stochastic_gradient_descent.zero_grad()
            predictions = self.lr_pytorch(inputs)
            
            loss = mse_loss_function(predictions,labels)
            loss.backward()
            stochastic_gradient_descent.step()
            
                                                        ############################################
                                                        ############### Running Demo ###############

###########################
####### 2 Variables #######
"""
x = [[1,2],[3,4],[5,4],[6,7],[9,10],[10,2]]
y = [6,60,120,336,90,80]
test = Variable(torch.from_numpy(np.array([100,10],dtype=np.float32)))
Model = linearRegression(2,1)
Model.fit(x,y,1000,0.001)
prediction = Model.forward(test) 
print(prediction)
"""

###########################
####### 3 Variables #######
"""
x = [[1,2,3],[3,4,5],[5,4,6],[6,7,8],[9,10,1],[10,2,4]]
y = [6,60,120,336,90,80]
test = Variable(torch.from_numpy(np.array([100,10,1],dtype=np.float32)))
Model = linearRegression(3,1)
Model.fit(x,y,1000,0.01)
prediction = Model.forward(test) 
print(prediction)
"""

                                                        ############################################
                                                        #################### Note ##################

# In case of reciving NaN as output, tune the Learning Rate or Normalize the data.
