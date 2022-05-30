def initalize_model():
    
    from tensorflow.keras import layers
    from tensorflow.keras import models
    model = models.Sequential()

    ### Rescaling Layer ###
    model.add(layers.Rescaling(1./255, input_shape = (img_height, img_width, 3))) # check this may need to divide by the image size
    
    ### First Convolution & Max Pooling ###
    model.add(layers.Conv2D(8, (4,4), activation = 'relu', padding = 'same'))
    model.add(layers.MaxPool2D(pool_size = (2,2)))

    ### Second Convolution & MaxPooling
    model.add(layers.Conv2D(16, (3,3), activation='relu', padding='same'))
    model.add(layers.MaxPool2D(pool_size=(2,2)))

    ### Flattening
    model.add(layers.Flatten())

    ### One Fully Connected layer - "Fully Connected" is equivalent to saying "Dense"
    model.add(layers.Dense(10, activation='relu'))

    ### Last layer - Classification Layer with 6 outputs corresponding to 6 art styles
    model.add(layers.Dense(6, activation='softmax'))
    
    ### Model compilation
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam', 
                  metrics=['accuracy'])
    
    return model
