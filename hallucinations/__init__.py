import webbrowser
from pathlib import Path

from numba import jit
import numpy as np
import matplotlib.pyplot as plt


__version__ = '0.1.3'
home = str(Path.home())


@jit
def mandelbrot(size, iterations):
    m = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            c = (-2 + 3. / size * j +
                 1j * (1.5 - 3. / size * i))
            z = 0
            for n in range(iterations):
                if np.abs(z) <= 10:
                    z = z * z + c
                    m[i, j] = n
                else:
                    break
    return m


def generate_site(img):
    html_file = home + '/fractal.html'

    html = """
    <center>
        <h1 style="font-family: Verdana;">Do not do drugs!</h1>
        <img src="{}" width="50%">
    </center>
    """.format(img)

    with open(html_file, 'wt') as html_output:
        html_output.write(html)
    return html_file


def main():
    m = mandelbrot(1024, 500)
    plt.imsave('mandelbrot.png', np.log(m), cmap='magma')
    site = generate_site('mandelbrot.png')
    webbrowser.open(site, new=2, autoraise=True)
    print("A web browser should open soon.")
    print("If the browser does not open, you can copy and paste the following on your browser:")
    print("{}".format(site))


main()
