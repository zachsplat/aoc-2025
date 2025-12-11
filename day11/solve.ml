let memo = Hashtbl.create 10000

let rec blink stone steps =
  if steps = 0 then 1
  else
    let key = (stone, steps) in
    match Hashtbl.find_opt memo key with
    | Some v -> v
    | None ->
      let result =
        if stone = 0 then
          blink 1 (steps - 1)
        else
          let s = string_of_int stone in
          let len = String.length s in
          if len mod 2 = 0 then
            let left = int_of_string (String.sub s 0 (len / 2)) in
            let right = int_of_string (String.sub s (len / 2) (len / 2)) in
            blink left (steps - 1) + blink right (steps - 1)
          else
            blink (stone * 2024) (steps - 1)
      in
      Hashtbl.replace memo key result;
      result

let () =
  let line = input_line (open_in Sys.argv.(1)) in
  let stones = List.map int_of_string (String.split_on_char ' ' line) in
  let p1 = List.fold_left (fun acc s -> acc + blink s 25) 0 stones in
  let p2 = List.fold_left (fun acc s -> acc + blink s 75) 0 stones in
  Printf.printf "p1: %d\np2: %d\n" p1 p2
