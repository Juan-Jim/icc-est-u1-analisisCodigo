import java.util.Random;



public class BenchmarKing {
 
    private MetodosOrdenamiento mOrdenamiento;

        public BenchmarKing() {
            long currentMillis = System.currentTimeMillis();
            long currentNano = System.nanoTime();

            System.out.println(currentMillis);
            System.out.println(currentNano);

            mOrdenamiento = new MetodosOrdenamiento();
            int[] arreglo = generraArregloAleatorio(100000);

            Runnable tarea = ()-> mOrdenamiento.burbujaTradicional(arreglo);

            double tiempoDuracionMilis = medirContCurrentTimeMi(tarea);
            double tiempoDuracionNano = medirContNanoTime(tarea);

            System.out.println("Tiempo en milisegundos: " + tiempoDuracionMilis);
            System.out.println("Tiempo en nanosegundos: " + tiempoDuracionNano);
        }

        private int[] generraArregloAleatorio(int tamaño) {
            int[] arreglo = new int[tamaño];
            Random random = new Random();
            for(int i = 0; i < tamaño; i++) {
                arreglo[i] = random.nextInt(10000);
            }
            return arreglo;
        }   

        private double medirContCurrentTimeMi(Runnable tarea) {
            long inicio = System.currentTimeMillis();
            tarea.run();
            long fin = System.currentTimeMillis();
            return (fin - inicio) / 1000.0; 
        }


        private double medirContNanoTime(Runnable tarea) {
            long inicio = System.currentTimeMillis();
            tarea.run();
            long fin = System.currentTimeMillis();
            return (fin - inicio) / 1_000_000_000.0;
        }
}
