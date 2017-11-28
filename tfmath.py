import tensorflow as tf
a = tf.constant(3)
b = tf.constant(2)
c = tf.add(a,b,'add')
d = tf.subtract(c,b,'subtract')
sess = tf.Session()
print('c - b =',sess.run(d))
print('a + b =',sess.run(c))

sess.close()