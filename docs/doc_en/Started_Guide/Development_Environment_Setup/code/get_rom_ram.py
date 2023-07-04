import gc
import uos

res = uos.statvfs("/usr")
res = list(res)
print('Obtain file system status information:', res)
print('F_bsize - File system block size, in bytes：', res[0])
print('F_bfree - Number of available blocks：', res[3])
print('Total remaining space {} bytes'.format(res[0] * res[3]))
print('Total remaining space {} MB'.format((res[0] * res[3]) / 1024 / 1024))

mem = gc.mem_free()
print('Remaining RAM space:{}KB'.format(mem / 1024))
