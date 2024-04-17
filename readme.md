# MCSRSI: a publicly dataset for Mesoscale Convective System Detection
## Introudction
MCSRSI is a dataset based on Fengyun-4A(FY-4A) for mesoscale convective system detection task. It is comprised of 8157 visible channel images in China region from FY-4A of shape $800 \times 1280$, ranging from January 2018 to December 2018. The time between acquisitions is 15 minutes. After calibrate the 12th channel of FY-4A’s L1 data, we acquire visible channel image as model's input. With the help of domain experts, we utilize brightness temperature threshold and radar echo intensity to manually label MCS regions. MCS exhibits significant differences in brightness temperature in different regions. In the southern of China, MCS regions generally have lower brightness temperature threshold, ranging from 215K to 225K. However, in the northern of China, they tend to range from 220K to 235K, and even reach around 240K in some cases. In terms of radar echo intensity, convective cloud typically has radar echo intensity greater than 25dbz. Finally, we export ground-truth from origin image by setting the MCS pixel to 255 and the non MCS pixel to 0.
## How to use
We provide a script for partitioning sequence data and provide three default partitioned datasets.
#### Download the dataset
The MCSRSI is about 20G. You can download the origin dataset from kuake cloud or google cloud
|||
|:---:|:---:|
|Google cloud|[MCSRSI]()|
|Kuake cloud|[MCSRSI]()|

#### Divide the dataset
You can run the spilt.py to divide MCSRSI into different sequence dataset. For example, you can exec the follow command to generate an image sequence with a length of 6 and an interval of 30min.   
```
python split.py --frames 6 --timesteps 30 --path The output path
```

#### A example of an image sequence with a length of 6 and an interval of 30min

```
{
 "201801": {
  "train": [
        [
         "20180112090000_20180112091459.png",
         "20180112091500_20180112092959.png",
         "20180112093000_20180112093416.png",
         "20180112094500_20180112094916.png",
         "20180112100000_20180112101459.png",
         "20180112101500_20180112101916.png"
        ]
        ....
   ]
   "valid":...
   "test":...
 }
 "201802":...
}
```
