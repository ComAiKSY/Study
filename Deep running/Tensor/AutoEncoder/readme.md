1. Network
    Auto Encoder
    Dimensions k = 32

2. Input & Output Layer
    Encoder
        Input : 28*28 = 784
        Output : 32
        Activation Function : tanh
    Decoder
        Input : 32
        Output : 28*28 = 784
        Activation Function : None

3. Object Function
    MSE

4. Hidden Layer
    Each 2
    Node : 200
    Activation Function : ReLU

5. Optimization Algorithm
    ADAM