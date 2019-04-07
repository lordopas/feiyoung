import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Calendar;


public class Password {
    public static void main(String[] args) throws NoSuchAlgorithmException {
        String password = "密码填这里";
        System.out.println("--------------------------------");
        for (int i = 1; i < 32; i++) {
            System.out.println(i+"="+getPasswd(password,i));
        }
        System.out.println("--------------------------------");
    }

    public static String getPasswd(String ps) throws NoSuchAlgorithmException{
        int x = Calendar.getInstance().get(Calendar.DATE);
        return getPasswd(ps,x);
    }

    public static String getPasswd(String ps ,int date) throws NoSuchAlgorithmException {
        byte[] passwdbyte = ps.getBytes();
        int len = ps.length();
        byte[] passwdToken = new byte[len];
        byte[] dateToken = getDateToken(date);

        int index1 = 0;
        int index2 = 0;
        for (int i = 0; i < len; i++) {
            index1 += 1 & 255;
            index1 %= 256;
            index2 += dateToken[index1] & 255;
            index2 %= 256;
            byte temp = dateToken[index1];
            dateToken[index1] = dateToken[index2];
            dateToken[index2] = temp;

            int index = dateToken[index1] + dateToken[index2] & 255;
            index %= 256;
            passwdToken[i] = (byte) (dateToken[index] ^ passwdbyte[i]);
        }
        byte[] passwd = MessageDigest.getInstance("MD5").digest(passwdToken);

        StringBuffer password = new StringBuffer();
        for (int i = 0; i < passwd.length; i++) {
            String hex = Integer.toHexString(passwd[i] & 255);
            if(hex.length()==1) {
                password.append('0');
            }
            password.append(hex);
        }

        return password.toString();
    }



    private static byte[] getDateToken(){
        // 获取今天是几日，比如今天是3月29日则返回29
        int x = Calendar.getInstance().get(Calendar.DATE);
        return getDateToken(x);
    }

    private static byte[] getDateToken(int x) {
        String word = "";
        switch (x) {
            case 1:
                word = "1430782659";
                break;
            case 2:
                word = "0267854319";
                break;
            case 3:
                word = "9173268045";
                break;
            case 4:
                word = "3401978562";
                break;
            case 5:
                word = "8174069325";
                break;
            case 6:
                word = "8076142539";
                break;
            case 7:
                word = "8957612403";
                break;
            case 8:
                word = "4573819602";
                break;
            case 9:
                word = "3829507461";
                break;
            case 10:
                word = "9356078241";
                break;
            case 11:
                word = "4791250368";
                break;
            case 12:
                word = "6721895340";
                break;
            case 13:
                word = "1938567204";
                break;
            case 14:
                word = "4195768023";
                break;
            case 15:
                word = "2508479316";
                break;
            case 16:
                word = "7029183654";
                break;
            case 17:
                word = "1876354092";
                break;
            case 18:
                word = "1785043926";
                break;
            case 19:
                word = "6178093542";
                break;
            case 20:
                word = "5643712089";
                break;
            case 21:
                word = "1958627043";
                break;
            case 22:
                word = "9572314608";
                break;
            case 23:
                word = "0841267953";
                break;
            case 24:
                word = "7415038296";
                break;
            case 25:
                word = "5364107982";
                break;
            case 26:
                word = "1328760549";
                break;
            case 27:
                word = "1420698537";
                break;
            case 28:
                word = "7368240195";
                break;
            case 29:
                word = "8314902567";
                break;
            case 30:
                word = "0456897213";
                break;
            case 31:
                word = "0954761238";
                break;
            default:
                return null;
        }
        int len = word.length();
        byte[] wordbyte = new byte[len];

        // 将字符串转化成数字数组  e.g："0954761238" ==> {0,9,5,4,7,6,1,2,3,8}
        for (int i = 0; i < len; i++) {
            wordbyte[i] = (byte) Integer.parseInt(String.valueOf(word.charAt(i)));
        }

        byte[] token = new byte[256];
        // 初始化
        for (int i = 0; i < 256; i++) {
            token[i] = (byte) i;
        }
        int index = 0;
        for (int i = 0; i < 256; i++) {
            index += token[i] + wordbyte[i % len] & 255;
            index %= 256;
            byte temp = token[i];
            token[i] = token[index];
            token[index] = temp;
        }
        return token;
    }
}