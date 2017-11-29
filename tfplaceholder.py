import tensorflow as tf
x = tf.placeholder(tf.int32,shape=[3],name='X')
y = tf.placeholder(tf.int32,shape=[3],name='Y')
sum_x = tf.reduce_sum(x,name='sum_x')
sess = tf.Session()
print("Sum X:",sess.run(sum_x,feed_dict={x:[300,200,100]}))
sess.close()