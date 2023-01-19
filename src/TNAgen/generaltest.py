from Generator import Generator
from gwpy.timeseries import TimeSeries
import time
import matplotlib.pyplot as plt
import numpy as np

def testGenerator():
    generator = Generator()
    generator.generate("Helix", 100)
    generator.save_as_png("src/data/sanity_images")
    generator.save_as_hdf5("src/data/sanity_images", "mydata", clear_queue=True)

def testRest():
    filepath = "src/data/sanity_images/mydata.hdf5"
    channel1 = "Chirp_timeseries_0"

    strain = TimeSeries.read(filepath, channel1)
    strain.sample_rate = 4096
    plt.plot(strain, 'forestgreen')
    plt.xlabel("Time (Seconds)")
    plt.savefig("src/data/sanity_images/test1.png")
    plt.close()

def testSpectrogram():
    filepath = "src/data/sanity_images/mydata.hdf5"
    channel1 = "Chirp_timeseries_0"

    strain = TimeSeries.read(filepath, channel1)

    fs = 4096

    NFFT = int(fs/16.)
    NOVL = int(NFFT*15./16)

    window = np.blackman(NFFT)
    spec_cmap='viridis'
    plt.figure(figsize=(8.5, 7))
    spec_H1, freqs, bins, im = plt.specgram(strain, NFFT=NFFT, Fs=fs, window=window,
        noverlap=NOVL, cmap=spec_cmap, scale='linear',mode='magnitude')
    plt.ylim(0,4096//2)
    plt.xlabel('time (s)',fontsize=14)
    plt.ylabel('frequency (Hz)',fontsize=14)
    plt.show()

if __name__ == "__main__":
    testGenerator()
    #testRest()
    #testSpectrogram()

    
