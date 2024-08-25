import matplotlib.pyplot as plt

def plotAlpha(df, title, ylim=None):
    fig = plt.figure(figsize=(15,8))
    for c in df.columns:
        plt.plot(df[c], label=f"k = {c}")
    plt.legend()
    plt.title(title)
    plt.xlabel("r")
    plt.grid()
    plt.ylabel("Alpha(r)")
    if ylim is not None:
        plt.ylim(0,ylim)
    plt.show()

def plotBeta(df, title, ylim1=None, ylim2 = None):
    fig = plt.figure(figsize=(15,8))
    plt.plot(df, label=f"m", marker='o')
    plt.title(title)
    plt.xlabel("m")
    plt.grid()
    if ylim1 is not None:
        plt.ylim(ylim1, ylim2)
    plt.ylabel("Beta(m,0)")
    plt.show()

def subplotAlphaBeta(alpha, beta, title, beta_ylim=None, alpha_ylim=None):
    fig, axs = plt.subplots(1,2, figsize=(18,7))
    for c in alpha.columns:
        axs[0].plot(alpha[c], label=f"k = {c}")
    
    axs[0].legend()
    axs[0].set_title('Alpha(r) vs r')
    axs[0].set_xlabel("r")
    axs[0].grid()
    axs[0].set_ylabel("Alpha(r)")
    if alpha_ylim is not None:
        axs[0].set_ylim(0, alpha_ylim)

    axs[1].bar(beta.index, height=beta.values, color = 'tab:orange')
    axs[1].plot(beta.index, beta.values, label=f"m", marker='^', linestyle='--')
    axs[1].set_title('Beta(m, 0) vs m')
    axs[1].set_xlabel("m")
    axs[1].grid()
    if beta_ylim is not None:
        axs[1].set_ylim(0, beta_ylim)
    axs[1].set_ylabel("Beta(m,0)")

    plt.suptitle(title, fontsize=16)
    plt.show()