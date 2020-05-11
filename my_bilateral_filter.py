def my_bilateral_filter(ImgNoisy, window_size = 3 , sigma_d = 4, sigma_r = 40):
    # sigma_d : smoothing weight factor
    # sigma_r : range weight factor
    
    height = ImgNoisy.shape[0]
    width = ImgNoisy.shape[1]
    # Initialize the filtered image:
    filtered_image = np.empty([height,width])
    # Starting looping and processing the orginal noisy and assigning values to the new filtered image
    window_boundary = int(np.ceil(window_size/2))
    for i in range(height):
        for j in range(width):
            
            normalization_counter = 0
            filtered_pixel = 0

            for k in range(i - window_boundary, i + window_boundary):
                for l in range(j - window_boundary, j + window_boundary):
                    # Apply window boundary conditions    
                    if (k >= 0 and k < height and l >= 0 and l < width):
                        # Calculate smoothing weight :
                        smoothing_weight_dist = math.sqrt(np.power((i - k), 2) + np.power((j - l), 2))
                        smoothing_weight = math.exp(-smoothing_weight_dist/(2 * (sigma_s ** 2)))
                        
                        # Calculate range weight :
                        range_weight_dist = (abs(int(imgNoisy[i][j]) - int(imgNoisy[k][l]))) ** 2
                        range_weight = math.exp(-range_weight_dist /(2 * (sigma_r ** 2)))
                        # Calculate combined weight, perform summation and normalization operations
                        bilateral_weight = smoothing_weight * range_weight

                        neighbor_pixel = imgNoisy[k, l]

                        filtered_pixel += neighbor_pixel * bilateral_weight

                        normalization_counter += bilateral_weight

            filtered_pixel = filtered_pixel / normalization_counter
            
            filtered_image[i][j] = int(round(filtered_pixel))

    return filtered_image  
