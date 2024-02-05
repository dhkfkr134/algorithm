-- ifnull(컬럼or데이터, null일때 넣을값)
SELECT PT_NAME, PT_NO, GEND_CD, AGE, ifnull(TLNO,'NONE') TLNO
from PATIENT
where AGE<=12 and GEND_CD='W'
order by AGE desc, PT_NAME asc