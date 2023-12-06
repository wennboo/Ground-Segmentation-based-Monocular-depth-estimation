clear;
clc;
src_dir=strcat('./realPics_t3/ransacTest_image.bin');%绝对路径
img = imread("./realPics_t3/ransacTest_image.png");
r= img(:,:,1);

g= img(:,:,2);
b= img(:,:,3);
r2 =dec2bin(reshape(r,[1 480*640]));
g2 =dec2bin(reshape(g,[1 480*640]));
b2 =dec2bin(reshape(b,[1 480*640]));
rgb16 = uint8(zeros(1,480*640*2));
for k = 1:480*640
    im1= bin2dec([r2(k,1:5),g2(k,1:3)]);
    im2= bin2dec([g2(k,4:6),b2(k,1:5)]);
    rgb16(1,(2*k-1)) =uint8(im1);
    rgb16(1, 2*k) = uint8(im2);
end
fid=fopen(src_dir,'w');%打开文件
for i =1:480*640*2
    fwrite(fid,rgb16(i));%写入i并换行
end
fclose(fid);%关闭文件