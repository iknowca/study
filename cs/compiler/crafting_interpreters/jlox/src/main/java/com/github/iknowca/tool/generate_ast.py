def define_visitor(f, base_name, class_name, field_list):
    f.write("  interface Visitor<R> {")
    f.write("\n")
    for field in field_list:
        type_name = field.split(" ")[0].strip()
        f.write("    R visit" + type_name + class_name + "(" + type_name + " " + base_name.lower() + ");")
        f.write("\n")
    f.write("  }")
    f.write("\n")

def define_type(f, base_name, class_name, field_list):
    f.write("  static class " + class_name + " extends " + base_name + " {")
    f.write("\n")

    #생성자
    f.write("    " + class_name + "(" + field_list + ") {")
    f.write("\n")
    fields = field_list.split(", ")
    for filed in fields:
        name = filed.split(" ")[1]
        f.write("      this." + name + " = " + name + ";")
        f.write("\n")
    f.write("    }")
    f.write("\n")

    f.write("    @Override")
    f.write("\n")
    f.write("    <R> R accept(Visitor<R> visitor) {")
    f.write("\n")
    f.write("      return visitor.visit" + class_name + base_name + "(this);")
    f.write("\n")
    f.write("    }")


    # 멤버 필드
    for filed in fields:
        name = filed.split(" ")[1]
        f.write("\n    final " + filed.split(" ")[0] + " " + name + ";")
    f.write("\n")
    f.write("  }")
    f.write("\n")


def define_ast(output_path, base_name, classes):
    with open(output_path + "/" + base_name + ".java", "w") as f:
        f.write("package com.github.iknowca.jlox;")
        f.write("\n")
        f.write("import java.util.List;")
        f.write("\n")
        f.write("abstract class " + base_name + " {")
        f.write("\n")

        define_visitor(f, base_name, base_name, classes)
        f.write("\n")

        for class_def in classes:
            define_type(f, base_name, class_def.split(":")[0].strip(), class_def.split(":")[1].strip())
            f.write("\n")

        f.write(" abstract <R> R accept(Visitor<R> visitor);")
        f.write("\n")
        f.write("\n")
        f.write("}")
        f.write("\n")

if __name__ == '__main__':
    output_path = "../jlox"
    define_ast(output_path, "Expr", [
        "Binary     : Expr left, Token operator, Expr right",
        "Grouping   : Expr expression",
        "Literal    : Object value",
        "Unary      : Token operator, Expr right"
    ])
