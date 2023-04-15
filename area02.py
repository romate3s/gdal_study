from osgeo import osr
import numpy as np
from osgeo import gdal

# 打开栅格数据集
raster = gdal.Open('JJJ_ISA1000m_update.tif')

# 获取栅格图层和地理变换参数
band = raster.GetRasterBand(1)
geotransform = raster.GetGeoTransform()

# 获取栅格图层的投影信息
proj = raster.GetProjection()
srs = osr.SpatialReference(wkt=proj)

# 计算栅格像素的面积
cell_width = geotransform[1]
cell_height = geotransform[5]
cell_area = np.abs(cell_width * cell_height)

# 计算所有栅格像素的总面积
band_array = band.ReadAsArray()
total_area = np.sum(np.where(band_array != band.GetNoDataValue(), cell_area, 0))

# 输出栅格面积
print('Raster area: {:.2f} square meters'.format(total_area))
