# Потоки в Питоне

- class threading.Thread( group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
  - group - не реализован еще, не используется, None
  - target - функция, исполнение которой прдполагается в потоке
  - name - название потока
  - arg - позиционные аргументы, подаваемые на вход в функцию
  - kwargs - наименованные аргументы, подаваемые на вход в функцию
  - daemon - демоничность потока, определяет то будет ли он закрыт если не осталось недемонических потоков, т.е. когда у нас остаются только демонические потоки - интерпретатор завершает свою работу. Пока у нас есть хотя-бы один недемонический поток, интерпретатор не закрывется.  

Методы:
   - th.start()
   - th.join(timeout=None) - позволяет заблокировать выполнение текущего потока, до тех пор пока не выполниться поток th (иногда нужно дождаться выполнение определенного потока)
   - th.run()
   - th.name - удобно для логирования
   - th.is_alive()  - поток живой или нет
   - th.ident - айдишник потока внутри питона
   - th.native_id - айдишник поток в рамках операционной системы, после завершения потока его айдишник может присвоиться другому потоку
   - th.daemon - является  ли поток демоническим

Когда мы объявлем внутри кода класс threading - сам поток не создается, но создается питонячий объект. Поток запускается через start.

GIL - не позволяет более чем одному потоку выполняться в каждый момент.  Потоки системные, если мы создали много потоков, система может назначить каждому ядру по одному потоку. Но GIL блокировшик (Mutex), которые позволяет выполняться только по одному потоку. 

CPU-bond задачи - привязаны к CPU, IO-bond - в основном привязаны в вводу и выводу (отправка по сети и тп). На CPU-bond в оновном задачи подсчета, на таких задачах GIL не позволяет нам распаралеливание. IO-bond задачи не блокируются GIL, поэтому если у нас задача ввода-вывода мы можем распаралелить стандартными средствами питона. Race Condition - состояния гонки, потоки будут выполняться в правильном порядке. 
Иногда в каких то библиотеках на тяжелые вычисления GIL отпускается (например есди  мы вычисляем кеш от какой-то длинной строки), после того как эти вычисления завершаются, питон обратно запрашивает GIL. Через каждый определенный промежуток времени поток, который захватид GIL проверяет, надо ли его освободить. Т.е. в потоке выполняются определнные куски кода, и после каждого куска проверяется надо ли освоботь GIL.  Другие потоки могут выставить какие-то флаги если им нужен GIL. 

Можно ввесит переменные только внутри одного потока:
  ```
  my_data = threading.local()
  m_data.x = 20
  
  ```
Cинхронизация
 - threading.Lock - классический mutex, бинарный семафор. Его можно захватить или отпустить, захваченный Lock может быть только одним потоком, другой поток не может схватить данный Lock; 
 - threading.RLock -  Lock, который может перезахватить, но перезахватить его может только один и тот же поток;
 - threading.Semaphore - позволяет  некоему количеству потоков захватить некий ресурс, можно задать количество потоков, которые могут захватить один Semaphore. Например, у нас есть база данных к которой мы обращаемся из разных потоков и  мы не хотим чтобы количество обращений в единиуц времени не первышало определенное количество;
 - threading.BoundedSemaphore - обычный Semaphore, но он проверяет количество освобождений этого семафора. Если количество освобождений превышает количество захватов, то будет выкидывать Exception;
 - threading.Event - событие на которые могут подписаться потоки, и когда оно происходит в другом потоке  все потоки, которые подписались на данное событие получают уведомление и могут стартовать с этой точки; 
 - threading.Timer - таймер который течет внутри отдельного потока, и поток стартует после того как таймер закончится;
 - threading.Barrier - примитив синхронизации, который не пускает потоки работать дальше, пока не наберется какое-то предопределенное количество;
