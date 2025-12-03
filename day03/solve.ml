let () =
  let ic = open_in Sys.argv.(1) in
  let n = in_channel_length ic in
  let s = really_input_string ic n in
  close_in ic;

  (* part 1: find all mul(X,Y) *)
  let re = Str.regexp {|mul(\([0-9]+\),\([0-9]+\))|} in
  let sum1 = ref 0 in
  let pos = ref 0 in
  (try while true do
    let _ = Str.search_forward re s !pos in
    let a = int_of_string (Str.matched_group 1 s) in
    let b = int_of_string (Str.matched_group 2 s) in
    sum1 := !sum1 + a * b;
    pos := Str.match_end ()
  done with Not_found -> ());
  Printf.printf "p1: %d\n" !sum1;

  (* part 2: track do/don't *)
  let enabled = ref true in
  let sum2 = ref 0 in
  let i = ref 0 in
  while !i < String.length s - 4 do
    if !i < String.length s - 7 && String.sub s !i 7 = "don't()" then begin
      enabled := false;
      i := !i + 7
    end else if !i < String.length s - 4 && String.sub s !i 4 = "do()" then begin
      enabled := true;
      i := !i + 4
    end else if !enabled then
      incr i
    else begin
      (try
        let _ = Str.search_forward re s !i in
        if Str.match_beginning () = !i then begin
          let a = int_of_string (Str.matched_group 1 s) in
          let b = int_of_string (Str.matched_group 2 s) in
          sum2 := !sum2 + a * b;
          i := Str.match_end ()
        end else
          incr i
      with Not_found -> i := String.length s)
    end
  done;
  Printf.printf "p2: %d\n" !sum2
