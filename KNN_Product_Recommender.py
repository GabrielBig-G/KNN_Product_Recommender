# Import math module
# Needed for square root calculations
import math


# Product catalog

# Feature order:
# [Price_Tier,
#  Category_Weight,
#  Review_Score_Avg,
#  Return_Rate_Inverse]

catalog_matrix = {

    "ITEM_ID_88": [

        0.20,
        0.90,
        0.85,
        0.95
    ],

    "ITEM_ID_12": [

        0.85,
        0.15,
        0.90,
        0.70
    ],

    "ITEM_ID_44": [

        0.25,
        0.80,
        0.75,
        0.90
    ],

    "ITEM_ID_31": [

        0.60,
        0.40,
        0.88,
        0.80
    ],

    "ITEM_ID_72": [

        0.15,
        0.95,
        0.92,
        0.97
    ]
}

def get_user_profile():
    """
    Collects user preference values
    and validates them.
    """

    # Empty list that will store
    # the user's vector
    user_profile = []

    # List of feature names
    feature_names = [

        "Price Tier",

        "Category Weight",

        "Review Score Average",

        "Return Rate Inverse"
    ]

    # Loop through each feature
    for feature in feature_names:

        while True:

            try:

                # Ask user for a value
                value = float(

                    input(
                        f"Enter {feature} "
                        f"(0.0 - 1.0): "
                    )
                )

                # Check normalization constraint
                if 0.0 <= value <= 1.0:

                    # Save value
                    user_profile.append(value)

                    # Exit validation loop
                    break

                else:

                    print(
                        "Error: Value must be "
                        "between 0.0 and 1.0"
                    )

            except ValueError:

                print(
                    "Error: Please enter "
                    "a valid number."
                )

    # Ask for K value
    while True:

        try:

            k = int(

                input(
                    "\nEnter K "
                    "(number of recommendations): "
                )
            )

            # K must be positive
            if k > 0:

                break

            else:

                print(
                    "Error: K must be "
                    "greater than zero."
                )

        except ValueError:

            print(
                "Error: Enter a valid integer."
            )

    # Return both values
    return user_profile, k

def calculate_distance(
    user_profile,
    product_vector
):
    """
    Calculates Euclidean Distance
    between the user profile and
    a product vector.
    """

    # Start accumulator at zero
    squared_sum_accumulator = 0.0

    # Loop through each dimension
    for vector_index in range(
        len(user_profile)
    ):

        # Calculate difference
        delta = (

            user_profile[vector_index]

            -

            product_vector[vector_index]
        )

        # Square difference
        squared_sum_accumulator += (
            delta * delta
        )

    # Apply square root
    final_distance = math.sqrt(
        squared_sum_accumulator
    )

    return final_distance

def build_distance_matrix(user_profile):
    """
    Calculates distance between the
    user profile and every product.
    """

    # Create empty distance list
    calculated_distance_matrix = []

    print(
        "\nComputing Multidimensional "
        "Geometric Euclidean Vector Distances:"
    )

    # Loop through every product
    for product_id, product_vector in catalog_matrix.items():

        # Calculate distance
        distance = calculate_distance(
            user_profile,
            product_vector
        )

        # Save result as tuple
        calculated_distance_matrix.append(

            (
                product_id,
                distance
            )
        )

        # Display result
        print(
            f"-> Evaluated Profile Metric "
            f"Distance [{product_id}] "
            f"-> Separation Score Value: "
            f"{distance:.4f}"
        )

    # Return completed matrix
    return calculated_distance_matrix

def sort_distance_matrix(
    calculated_distance_matrix
):
    """
    Sorts the distance matrix
    from smallest distance
    to largest distance.
    """

    # Get total number of items
    matrix_length = len(
        calculated_distance_matrix
    )

    # Outer loop
    for i in range(matrix_length):

        # Assume current position
        # contains smallest value
        smallest_index = i

        # Search remaining elements
        for j in range(
            i + 1,
            matrix_length
        ):

            # Compare distances
            if (
                calculated_distance_matrix[j][1]
                <
                calculated_distance_matrix[
                    smallest_index
                ][1]
            ):

                smallest_index = j

        # Swap positions
        (
            calculated_distance_matrix[i],
            calculated_distance_matrix[
                smallest_index
            ]
        ) = (
            calculated_distance_matrix[
                smallest_index
            ],
            calculated_distance_matrix[i]
        )

    # Return sorted matrix
    return calculated_distance_matrix

def get_k_nearest_neighbors(
    sorted_distance_matrix,
    k
):
    """
    Extracts the K nearest products
    and displays recommendations.
    """

    # Empty list for neighbors
    nearest_neighbors = []

    # Loop through first K elements
    for index in range(k):

        # Prevent index errors
        if index < len(
            sorted_distance_matrix
        ):

            nearest_neighbors.append(

                sorted_distance_matrix[index]
            )

    print(
        "\nExtracting Nearest Matching "
        "Architectural Neighbors..."
    )

    print("-" * 68)

    print(
        "RANK | PRODUCT SKU | "
        "EUCLIDEAN DISTANCE VALUE | "
        "MATCH CONFIDENCE"
    )

    print("-" * 68)

    # Display recommendations
    for rank in range(
        len(nearest_neighbors)
    ):

        product_id = (
            nearest_neighbors[rank][0]
        )

        distance = (
            nearest_neighbors[rank][1]
        )

        confidence = (
            (1 - distance) * 100
        )

        # Prevent negative percentages
        if confidence < 0:

            confidence = 0

        print(
            f"{rank + 1} | "
            f"{product_id} | "
            f"{distance:.4f} | "
            f"{confidence:.2f}%"
        )

    print("-" * 68)

    print(
        f"Recommendation Pipeline "
        f"Execution Success: "
        f"{len(nearest_neighbors)} "
        f"items identified"
    )

    return nearest_neighbors

def main():
    """
    Main KNN recommendation engine.
    """

    print(
        ">>> INITIALIZING VECTOR "
        "CALCULATION MATRIX ENGINE..."
    )

    # Get user profile and K
    user_profile, k = get_user_profile()

    print(
        f"\nTarget Reference "
        f"Profile Vector Parameters Input: "
        f"{user_profile}"
    )

    print(
        f"Target Requested "
        f"Neighborhood Extent "
        f"Configuration Value (K): {k}"
    )

    # Build distance matrix
    distance_matrix = build_distance_matrix(
        user_profile
    )

    # Sort matrix manually
    sorted_matrix = sort_distance_matrix(
        distance_matrix
    )

    # Extract recommendations
    get_k_nearest_neighbors(
        sorted_matrix,
        k
    )

if __name__ == "__main__":

    main()