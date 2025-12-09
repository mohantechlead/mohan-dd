"use client";

// import { FC, ReactNode } from "react";
// import { useForm, SubmitHandler, FieldValues, UseFormReturn, FormProvider } from "react-hook-form";
// import { Button } from "@/components/ui/button";
// import { Label } from "@/components/ui/label";
// import { Input } from "@/components/ui/input";
// import { cn } from "@/lib/utils";

// interface FormField {
//   name: string;
//   label: string;
//   placeholder?: string;
//   type?: string;
// }

// interface FormProps<T extends FieldValues> {
//   fields: FormField[];
//   onSubmit: SubmitHandler<T>;
//   formMethods?: UseFormReturn<T>;
//   submitText?: string;
//   className?: string;
//   children?: ReactNode;
// }

// export const Form = <T extends FieldValues>({
//   fields,
//   onSubmit,
//   formMethods,
//   submitText = "Submit",
//   children,
//   className = "",
// }: FormProps<T>) => {
//   const methods = formMethods || useForm<T>();
//   const { handleSubmit, register, formState } = methods;
//   const { errors } = formState;

//   return (
//     <FormProvider {...methods}>
//     <form className={cn("grid grid-cols-2 gap-2", className)} onSubmit={handleSubmit(onSubmit)}>
//       {fields.map((field) => (
//         <div key={field.name} className="flex flex-col gap-1 max-w-3xl">
//           <Label htmlFor={field.name}>{field.label}</Label>
//           <Input
//             id={field.name}
//             type={field.type || "text"}
//             placeholder={field.placeholder}
//             // {...register(field.name as keyof T, { required: true })}
//           />
//           {errors[field.name as keyof T] && (
//             <span className="text-red-500 text-sm">This field is required</span>
//           )}
          
//         </div>
        
//       ))}
//       {children}

//       <Button type="submit">{submitText}</Button>
//     </form>
//     </FormProvider>
//   );
// };

"use client";

import { FormProvider, useForm } from "react-hook-form";
import { Button } from "./ui/button";
import { Input } from "./ui/input";
import { Label } from "./ui/label";
import { cn } from "@/lib/utils";

interface Field {
  name: string;
  label: string;
  type?: string;
  placeholder?: string;
}

interface FormProps<T> {
  fields: Field[];
  onSubmit: (values: T) => void;
  submitText: string;
  children?: React.ReactNode;
}

export function Form<T>({ fields, onSubmit, submitText, children }: FormProps<T>) {
  const methods = useForm<T>();

  return (
    <FormProvider {...methods}>
      <form
        className="flex flex-col gap-4"
        onSubmit={methods.handleSubmit(onSubmit)}
      >
        {fields.map((field) => (
          <div key={field.name} className="flex flex-col gap-1">
            <Label>{field.label}</Label>
            <Input
              type={field.type || "text"}
              placeholder={field.placeholder}
              {...methods.register(field.name as any)}
            />
          </div>
        ))}

        {children}

        <Button type="submit">{submitText}</Button>
      </form>
    </FormProvider>
  );
}

