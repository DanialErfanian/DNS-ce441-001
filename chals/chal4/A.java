public class MyClass {
    private static String mAskAmir = "S_V]L_N\036[VJ\036eB\017JYFH\017\003]FBn";

    private static String mAskAmirAgain = "\000gnhqs}(K\000tc`qge{;\0002 `!sd(J\000";

    private static String reverseEasyHash(String paramString) {
        char[] arrayOfChar = paramString.toCharArray();
        for (byte b = 0; b < arrayOfChar.length / 2; b++) {
//            char c = arrayOfChar[b];
//            arrayOfChar[b] = (char)(char)(arrayOfChar[arrayOfChar.length - b - 1] ^ 0x3E);
//            arrayOfChar[arrayOfChar.length - b - 1] = (char)(char)(c ^ 0x2F);
            char c = arrayOfChar[b];
            arrayOfChar[b] = (char) (char) (arrayOfChar[arrayOfChar.length - b - 1] ^ 0x2F);
            arrayOfChar[arrayOfChar.length - b - 1] = (char) (char) (c ^ 0x3E);
        }
        return new String(arrayOfChar);
    }

    private static String reverseHardHash(String paramString) {
        char[] arrayOfChar = paramString.toCharArray();
        byte b;
        for (b = 0; b < arrayOfChar.length / 2; b++) {
            char c = arrayOfChar[b];
            arrayOfChar[b] = (char) arrayOfChar[arrayOfChar.length - b - 1];
            arrayOfChar[arrayOfChar.length - b - 1] = (char) c;
        }
        for (b = 0; b < arrayOfChar.length; b++) {
            char ch1 = arrayOfChar[b];
            int count = 0;
            String amo = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ {},!";
            for (int i = 0; i < amo.length(); i++) {
                char ch2 = amo.charAt(i);
                if (((char) ch2 ^ ch2 >> b % 9) == ch1) {
                    count++;
                    arrayOfChar[b] = ch2;
                }
            }
            if (count != 1)
                arrayOfChar[b] = '?';
//            arrayOfChar[b] = (char)(char)(arrayOfChar[b] ^ c >> b % 9);
        }
        return new String(arrayOfChar);
    }


    private String generateParcham(String input2) {
        char[] arrayOfChar1 = "Amir, give me the parcham".substring(14, 16).toCharArray();
        char[] arrayOfChar2 = input2.substring(3, 11).toCharArray();
        arrayOfChar1[0] = (char) (char) (arrayOfChar1[0] ^ 0x36);
        arrayOfChar1[1] = (char) (char) (arrayOfChar1[1] ^ 0xD);
        arrayOfChar2[0] = (char) (char) (arrayOfChar2[0] ^ 0xA);
        arrayOfChar2[1] = (char) (char) (arrayOfChar2[1] ^ 0x6);
        arrayOfChar2[2] = (char) (char) (arrayOfChar2[2] ^ 0x45);
        arrayOfChar2[3] = (char) (char) (arrayOfChar2[3] ^ Character.MIN_VALUE);
        arrayOfChar2[4] = (char) (char) (arrayOfChar2[4] ^ 0x54);
        arrayOfChar2[5] = (char) (char) (arrayOfChar2[5] ^ 0x5B);
        arrayOfChar2[6] = (char) (char) (arrayOfChar2[6] ^ 0x46);
        arrayOfChar2[7] = (char) (char) (arrayOfChar2[7] ^ 0x48);
        return "No. parcham is parcham{" + new String(arrayOfChar1) + "_" + new String(arrayOfChar2) + "}";
    }

    public static void main(String args[]) {
        System.out.println(MyClass.reverseEasyHash(MyClass.mAskAmir));
        System.out.println(MyClass.reverseHardHash(MyClass.mAskAmirAgain));
        String amo1 = "Amir, give me the parcham";
        String amo2 = "?s it a 2??charact?r string?";
        System.out.println(new MyClass().generateParcham("Is it a 20-character string?"));
        System.out.println(new MyClass().generateParcham("Is it a 20 character string?"));
        System.out.println(new MyClass().generateParcham("Is it a 21 character string?"));
        System.out.println(new MyClass().generateParcham("Is it a 22 character string?"));
        System.out.println(new MyClass().generateParcham("Is it a 23 character string?"));
        System.out.println(new MyClass().generateParcham("Is it a 24 character string?"));
        System.out.println(new MyClass().generateParcham("Is it a 25 character string?"));
        System.out.println(new MyClass().generateParcham("Is it a 26 character string?"));
        System.out.println(new MyClass().generateParcham("Is it a 27 character string?"));
        System.out.println(new MyClass().generateParcham("Is it a 28 character string?"));
        System.out.println(new MyClass().generateParcham("Is it a 29 character string?"));
    }
}