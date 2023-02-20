def plot_multiple_subplots(df, df2, xaxis, yaxes, color1='blue', color2='red', size1=20, size2=10, shape1='o', shape2='o'):
    # Calculate the number of rows and columns needed for the subplots
    n_plots = len(yaxes)
    n_rows = int(n_plots ** 0.5)
    n_cols = int(n_plots ** 0.5)

    if n_rows * n_cols == n_plots:
        pass
    else:
        n_rows = n_rows+1


    # Create a figure with the calculated number of subplots
    fig, ax = plt.subplots(n_rows, n_cols, figsize=(10, 10))

    # Iterate over the yaxes and plot each one in a separate subplot
    for i, y in enumerate(yaxes):
        row = i // n_cols
        col = i % n_cols
        sns.lineplot(x=xaxis, y=df[y], data=df, ax=ax[row, col], label='Set 1', marker=shape1, markersize=size1, color=color1)
        sns.lineplot(x=xaxis, y=df2[y], data=df2, ax=ax[row, col], label='Set 2', marker=shape2, markersize=size2, color=color2)

    # Set the title for each subplot
    for i, ax in enumerate(fig.axes):
        if i < len(yaxes):
            ax.set_title(yaxes[i])

    # Adjust the layout and show the plot
    plt.tight_layout()
    plt.show()
