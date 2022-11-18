import java.sql.Connection;
import java.sql.DriverManager;


public class ConexaoBancoDeDados{

    static String driverJDBC = "org.gjt.mysql.Driver";
    static String url = "jdbc:mysql://localhost:3306/reservas";
    static String user = "root";
    static String senha = "root";

    public static void main(String[]    args){

        try{
            System.out.println("Carregando o Driver JDBC...");
            Class.forName(driverJDBC);
            System.out.println("Driver carregado com sucesso!!");
        } catch (Exception e)
        {
            System.out.println("Falha no carregamento!!");
        }

        try {
            System.out.println("Conectando ao banco...");
            Connection conexao = DriverManager.getConnection(url, user, senha); 
            System.out.println("Conexão efetuada com sucesso!!!");
            } catch (Exception e)
            {
                System.out.println("Falha na conexão!!");
            }

    }
}