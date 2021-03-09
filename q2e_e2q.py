import math

## Quaternion to Euler ##
def q2e(q):

	    # roll
        roll = math.atan2( 2*(q[0]*q[1] + q[2]*q[3]), 1 - 2*(q[1]**2 + q[2]**2) )

        # pitch
        sinp = -2.0 * (q[3] * q[1] - q[2] * q[0])
        if math.fabs(sinp) >= 1:
            # use 90 degrees if out of range
            pitch = math.copysign(math.pi / 2, sinp)
        else:
            pitch = math.asin(sinp)

		# yaw
        yaw = math.atan2( 2*(q[0]*q[3] + q[1]*q[2]), 1 - 2*(q[2]**2 + q[3]**2) )

        rpy = np.array([ [roll], [pitch], [yaw] ])

        return rpy

## Euler to Quaternion ##
def e2q(rpy):

            cr = math.cos(rpy[0] / 2)
            sr = math.sin(rpy[0] / 2)
            cp = math.cos(rpy[1] / 2)
            sp = math.sin(rpy[1] / 2)
            cy = math.cos(rpy[2] / 2)
            sy = math.sin(rpy[2] / 2)

            q = [0, 0, 0, 0]

            q[0] = cr * cp * cy + sr * sp * sy # w
            q[1] = sr * cp * cy - cr * sp * sy # x
            q[2] = cr * sp * cy + sr * cp * sy # y
            q[3] = cr * cp * sy - sr * sp * cy # z

            q = np.array([ [q[0]], [q[1]], [q[2]], [q[3]] ])

            return q

## Test ##

rpy = [0, 0, math.pi/2]
print(rpy)

q = e2q(rpy)
print(q)

Re_rpy = q2e(q)
print(Re_rpy)